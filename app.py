import streamlit as st
import cv2
import numpy as np
from hand_detector import HandDetector
from utils import fingersUp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import ctypes
import time

# 🎛️ Set up page
st.set_page_config(
    page_title="🎛️ Gesture Volume Controller",
    layout="wide",
    page_icon="🖐️"
)

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🖐️ Gesture Volume Controller</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center;'>Control your system volume just by raising your fingers!</h4>",
    unsafe_allow_html=True,
)

# 🖥️ Setup system volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[0:2]

# 🎯 Sidebar controls
st.sidebar.title("⚙️ Settings")
run = st.sidebar.checkbox("📷 Start Camera", value=False)
show_info = st.sidebar.checkbox("📊 Show Info Panel", value=True)

FRAME_WINDOW = st.empty()
info_placeholder = st.sidebar.empty()

# ✋ Initialize Hand Detector
detector = HandDetector(detectionCon=0.75)

if run:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("🚫 Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)

        totalFingers = 0
        volume_percent = 0

        if lmList:
            finger_status = fingersUp(lmList)
            totalFingers = sum(finger_status)

            # 🎚️ Volume Mapping
            volume_percent = totalFingers * 20
            volume_scalar = volume_percent / 100
            volume.SetMasterVolumeLevelScalar(volume_scalar, None)

            # 🔊 Draw Volume Bar
            vol_bar = int(np.interp(volume_percent, [0, 100], [400, 150]))
            cv2.rectangle(frame, (50, 150), (85, 400), (50, 255, 50), 3)
            cv2.rectangle(frame, (50, vol_bar), (85, 400), (50, 255, 50), cv2.FILLED)

            # ✍️ Draw Text
            cv2.putText(frame, f'Fingers: {totalFingers}', (30, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)
            cv2.putText(frame, f'{volume_percent} % Volume', (30, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 0), 2)

            # ✅ Sidebar single update
            if show_info:
                info_placeholder.markdown(
                    f"""
                    <div style="padding:10px; border-radius:10px; background:#e0f7fa; color:#004d40; font-weight:bold;">
                    🖐️ Fingers Up: {totalFingers} <br>
                    🔊 Volume: {volume_percent}%
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        time.sleep(0.03)  # Slight pause for better performance

    cap.release()
else:
    st.info("✅ Camera is stopped. Enable from the sidebar to begin.")
