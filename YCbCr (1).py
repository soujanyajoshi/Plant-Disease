
#Import packages
import cv2
import numpy as np

#Start camera on the host-device
cap = cv2.VideoCapture('http://192.168.0.101:8080/video')

while True:
    
    #Kernel for erosion and dilation
    kernel=np.ones((5,5), np.uint8)
    
     # Take each frame
    _, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Convert BGR to YCrCb
    YCbCr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    
    
    '''
    Segmentation
    '''
    
    #Noise Reduction
    #Erosion
    img_erosion = cv2.erode(frame, kernel, iterations=2)
    
    #Dilation
    img_dilation = cv2.dilate(frame, kernel, iterations=2)
    
        
    #Opening 
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)   
    
    #Closing
    closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
      
    
    
    
    
    #Output windows
    #cv2.imshow('Erosion',img_erosion)
    #cv2.imshow('Dilation',img_dilation)
    cv2.imshow('Opening',opening)   
    cv2.imshow('Closing',closing)
    cv2.imshow('YCrCb',YCbCr)
    
    #If-Block to quit/terminate program
    if cv2.waitKey(25) &0xFF ==ord('q'):
        break

#Release the camera resource
cap.release()

#Close all windows opened
cv2.destroyAllWindows()