# 🖐️ Hand Gesture Volume Controller

A real-time hand gesture-based system to control system volume using your fingers! Built with **Python**, **OpenCV**, **Mediapipe**, and **Streamlit**, this app detects your hand gestures through your webcam and adjusts the system volume accordingly.

<br/>

---

## 🧠 How It Works

1. **Hand Detection**  
   - Uses Mediapipe’s real-time hand tracking solution.  
   - Identifies 21 landmarks on your hand.

2. **Finger Detection**  
   - Determines how many fingers are up (extended).  
   - Based on the number of fingers up, sets the system volume.

3. **Volume Control**  
   - Volume is mapped linearly from distance between thumb and index finger tips.  
   - Uses `pycaw` to interface with Windows system volume.

4. **Live Stream Interface**  
   - Streamlit displays the webcam feed with real-time gesture analysis.  
   - Side panel shows finger count and current volume level.

---

## 🖥️ Libraries Used

- opencv-python  
- mediapipe  
- streamlit  
- pycaw  
- numpy

---

## 🛠️ Features

- ✋ Real-time finger tracking  
- 🔊 Volume control based on gesture  
- 🎨 Live webcam feed with overlays  
- 📊 Sidebar showing:
  - Fingers up  
  - Volume percentage  
- 🌈 Smooth visuals and interface  
- 🖥️ Windows support (using `pycaw`)

---

## 📦 Requirements

Install all required dependencies from the provided file:

```bash
pip install -r Requirements.txt
```

## 🚀 How to Run
To launch the Streamlit app:
```bash
streamlit run app.py
```

- Make sure your webcam is connected.
- Allow browser access if prompted.
- Works best in a well-lit environment.

---

## 📁 Project Structure
```bash
📦 Hand-Gesture-Volume-Controller
    ├── app.py                 # Streamlit web app entry point
    ├── hand_detector.py       # Hand tracking logic using Mediapipe
    ├── utils.py               # Helper functions (volume mapping, finger detection)
    ├── Requirements.txt       # Python dependencies
    ├── README.md              # Project documentation
```
---

## 🔍 Volume Mapping Logic
- Calculates distance between thumb tip and index finger tip using Euclidean distance.
- Uses np.interp() to map that distance to a system volume range.

```bash
volume = np.interp(length, [20, 200], [0, 100])
```
---

## ✌️ Finger Counting Logic

- Uses Mediapipe’s 21 hand landmarks.
- Checks whether fingertips are above their corresponding knuckles (e.g., tip of index above PIP joint).
- Based on this logic, determines how many fingers are raised.
  
---

## 👥 Credits

- 👨‍💻 **Developer**: Abdul Rauf  

---

## 📬 Contact

For feedback, bugs, or questions, feel free to reach out:

- 📧 **Email**: connect2rauf17@gmail.com  
- 🐙 **GitHub**: [rauf17](https://github.com/rauf17)

---

## License

© 2025, **Abdul Rauf**  

This project is Distributed under the Creative Commons Attribution-NonCommercial 4.0 International Public License (CC BY-NC 4.0).

See the `LICENSE` file in the repository for the license text.

---
