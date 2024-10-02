import cv2 as cv
import numpy as np
import time
import poseestimationmodule as pm

cap = cv.VideoCapture('trainingVids/curls_1.mp4')

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img =  cap.read()
    img = cv.resize(img, (1280,720))
    #img = cv.imread('trainingVids/aiTrainer.png')
    
    img = detector.findPose(img, False)
    lmlist = detector.findPosition(img, False)
    #print(lmlist)
    if len(lmlist) != 0:
        # right arm
        angle = detector.findAngle(img, 12, 14, 16 )
        ## left arm
        #angle = detector.findAngle(img, 11, 13, 15 )
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))
        # print(angle, per)
        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        # Draw Bar
        cv.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv.rectangle(img, (1100, int(bar)), (1175, 650), color, cv.FILLED)
        cv.putText(img, f'{int(per)} %', (1100, 75), cv.FONT_HERSHEY_PLAIN, 4,
                    color, 4)
        # Draw Curl Count
        cv.rectangle(img, (0, 550), (150, 6000), (0, 255, 0), cv.FILLED)
        cv.putText(img, str(int(count)), (50, 660), cv.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 10)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (50, 100), cv.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 2)




    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()