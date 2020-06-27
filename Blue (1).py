

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    cl=np.array([36,0,0])#Green
    ch=np.array([70,255,255])#Green

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, cl, ch)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv',hsv)
    if cv2.waitKey(25) &0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()