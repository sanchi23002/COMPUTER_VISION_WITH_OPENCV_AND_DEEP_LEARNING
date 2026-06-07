import numpy as np
import cv2

def draw_circle(event,x,y,flag,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,255),-1)
           
cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_circle)

img = np.zeros([2048,2048,3],np.int8)
img[:,:,0]=100
img[:,:,1]=100

while(True):
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
        