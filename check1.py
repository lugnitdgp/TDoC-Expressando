import cv2
import numpy as np

img1 = cv2.imread('abc.jpg') #static Images
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(img,30,200)
contours,heirarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny edges',edged)
cv2.waitKey(0)

cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Contours',img)

ret,thresh1=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold',thresh1)
cv2.imshow('Binary Threshold Inverted',thresh2)
cv2.imshow('Truncated Threshold',thresh3)
cv2.imshow('Set to 0',thresh4)
cv2.imshow('Set to 0 Inverted',thresh5)


interrupt = cv2.waitKey(0) & 0xFF
if interrupt == 27: #ord returns the Unicode of 'q' quit
    cv2.destroyAllWindows()