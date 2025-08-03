def fingersUp(lmList):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    if len(lmList) == 0:
        return fingers

    # Thumb
    if lmList[tips[0]][1] > lmList[tips[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Fingers (index to pinky)
    for i in range(1, 5):
        if lmList[tips[i]][2] < lmList[tips[i] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers
