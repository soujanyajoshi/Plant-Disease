
import numpy as np 
import cv2 

im_width = 320
im_height = 240
cap = cv2.VideoCapture(0)

# The order of the colors is blue, green, red
lower_color_bounds = np.array([140, 255, 0])
upper_color_bounds = np.array([40,255,0])


while(True):
 ret,frame = cap.read()
 gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 mask = cv2.inRange(gray,lower_color_bounds,upper_color_bounds )
 mask_rgb = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
 frame = frame & mask_rgb
 
 cv2.imshow('Video',frame)
 
 if cv2.waitKey(25) &0xFF ==ord('q'):
     break

cap.release()
cv2.destroyAllWindows()
