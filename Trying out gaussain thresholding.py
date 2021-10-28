import numpy as np
import cv2
 

image = cv2.imread('bookpage.jpg')
cv2.imshow('Original', image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Grayscale', gray_image)


thresh1= cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,155,1)
thresh2= cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,3)
cv2.imshow("adaptive mean",thresh1)
cv2.imshow("gaussian thresh",thresh2)


cv2.waitKey(0)

cv2.destroyAllWindows()
