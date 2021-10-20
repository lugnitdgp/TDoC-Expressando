import cv2 as cv
import numpy as np
image=cv.imread('emma3.jpg')
cv.imshow("original",image)

# I have added this image in the task folder beacuse the sprecifications work different for different pictures. I thought these work fine for this picture.


gray_scale=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
gray_scale=cv.medianBlur(gray_scale,3)
edges=cv.adaptiveThreshold(gray_scale,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,5)
cv.imshow("edges",edges)
color=cv.bilateralFilter(image,5,250,250)
cartoon=cv.bitwise_and(color,color,mask=edges)
cv.imshow("final result",cartoon)
cv.waitKey(0)
cv.destroyAllWindows()