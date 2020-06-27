

import cv2
import numpy as np
from skimage.measure import compare_ssim


cap = cv2.VideoCapture('http://192.168.0.101:8080/video') #Input from IPCamera
#cap = cv2.VideoCapture(0) #WEbCam Input



score=0
while(1):
    
    #Kernel for erosion and dilation
    kernel=np.ones((5,5), np.uint8)

    # Take each frame
    _, frame = cap.read()    
    

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    

    cl=np.array([36,0,0])     #Green
    ch=np.array([70,255,255]) #Green

    #cl=np.array([0,0,0])     #Black
    #ch=np.array([15,15,15])  #Black  
        
    
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, cl, ch)   
       
    
    if cv2.waitKey(1) & 0xFF ==ord('y'):
        cv2.imwrite('test.jpg',mask)
        imageA=cv2.imread('abc2.jpg',0)
        imageB=cv2.imread('test.jpg',0)
        (score,diff)=compare_ssim(imageA,imageB,full=True)
        print('Captured')    
        
        #diff=cv2.subtract(imageA,imageB)
        #result = not np.any(diff)
        #If true, similar
    
    
       
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #img_dilation = cv2.dilate(res, kernel, iterations=2)
    #img_erosion  = cv2.erode(res, kernel, iterations=2)
    
    #cv2.imshow('AAA',img_dilation)
    #cv2.imshow('BBB',img_erosion)
    
    
    #Contours
    #Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity.  
    #im2, contours, hierarchy=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
    im2, contours, hierarchy=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count=0
    
    #Loop for displaying all significant contours 
    for i in range(len(contours)):
        if cv2.contourArea(contours[i])>100.0:
            count=count+1
            x,y,w,h=cv2.boundingRect(contours[i])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)    
        
    
    #canny=cv2.Canny(frame,20,60,1)
    #cv2.imshow('canny',canny)   
    
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('mask',mask)
    #cv2.imshow('gray',gray)
    cv2.imshow('res',res)
    #cv2.imshow('hsv',hsv)    
    
    
    if cv2.waitKey(25) &0xFF ==ord('q'):
        break
    
print(count)
print(score)
cap.release()
cv2.destroyAllWindows()
