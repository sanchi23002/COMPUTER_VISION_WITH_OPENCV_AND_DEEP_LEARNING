import cv2
import numpy as np

img = cv2.imread(r'C:/Users/Sanchita Ghosh/OneDrive/Desktop/ML important things/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while (True):
    cv2.imshow('puppy', img)
    if(cv2.waitKey(1) & 0xFF == 27):
        break

cv2.destroyAllWindows()