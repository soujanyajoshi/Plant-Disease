
import cv2
import numpy as np

#Start the default camera on deployable device
#cam = cv2.VideoCapture('http://192.168.0.101:8080/video')
#cam = cv2.VideoCapture('Apple.mp4')
#Webcam
cam = cv2.VideoCapture(0)

while True:
    
    #Read the frames 
    _,frame=cam.read()
    cv2.imshow('frame',frame)
    
    #Convert BGR to HSV
    #Changing color-space for easy identification of the object we are trying to find
    #HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #Lower and Upper HSV Values
    
    #cl=np.array([36,0,0])#Green
    #ch=np.array([70,255,255])#Green
    
    #cl=np.array([18,0,196])#Yellow
    #ch=np.array([36,255,255])#Yellow
    
    #cl=np.array([89,0,0])#Blue
    #ch=np.array([125,255,255])#Blue
    
    cl=np.array([0,100,100])#Red    
    ch=np.array([15,255,255])#Red
    
    #cl=np.array([5,55,55])#expt    
    #ch=np.array([15,255,255])#expt
    
    #cl=np.array([170,150,60]) #Red
    #ch=np.array([179,255,255])#Red
    
    #Mask the image by giving lower and upper ranges
    #mask=cv2.inRange(HSV, cl, ch)
    #Show the mask output
    #cv2.imshow('mask',mask)
    
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    
    #cv2.imshow('Bitwise',res)
    
    #Find contours
    #im2, contours, hierarchy=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)  
    
    #cv2.drawContours(frame, contours,-1,(0,255,0),3)
    
    '''
    #For the largest contour
    areas=[cv2.contourArea(c) for c in contours]
    max=np.argmax(areas)
    
    cnt=contours[max]
    x,y,w,h=cv2.boundingRect(cnt)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    count=0
    #Loop for displaying all significant contours
    for i in range(len(contours)):
        if cv2.contourArea(contours[i])>100.0:
            count=count+1
            x,y,w,h=cv2.boundingRect(contours[i])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
    '''
        
    #Show the frame with output
    cv2.imshow('frame',frame)
    
    #Quit the program
    if cv2.waitKey(25) &0xFF ==ord('q'):
        break
    
#Print the approx count
#print("Approx count is {}".format(count))
#Release cam connection
cam.release()
#Destroy all windows
cv2.destroyAllWindows()