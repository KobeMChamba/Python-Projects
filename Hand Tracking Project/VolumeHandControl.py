import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

##########################################
wCam, hCam = 640, 480
##########################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)  # We are using default parameters
# but increasing necessary confidence for detection


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()   # (-63.5, 0.0, 0.5)
# volume.SetMasterVolumeLevel(-20.0, None)
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volPer = 0
volBar = 320
success, img = cap.read()
height, width, channels = img.shape
print(height, width)  # 360 640

while True:
    success, img = cap.read()
    img = detector.findHands(img)  # Method we created
    lmList = detector.findPosition(img, draw=False)  # Draw is false because we
    # are already drawing with findHands
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])  # Tip of thumb and index

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        # Hand range 50 - 200
        # Volume Range -63 - 0

        vol = np.interp(length, [30, 160], [minVol, maxVol])
        volBar = np.interp(length, [30, 160], [320, 150])
        volPer = np.interp(length, [30, 160], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 320), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 320), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f' VOL: {int(volPer)} %', (20, 350), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)

    cv2.imshow("VolumeControl", img)
    cv2.waitKey(1)
