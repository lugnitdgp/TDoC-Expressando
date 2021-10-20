import cv2
import numpy as np 
img = cv2.imread('abc.jpg')

cv2.imshow("original",img)
img2 = cv2.resize(img, (400, 400))
cv2.imshow("Image", img2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("blur", blur)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
_, thresh_binary = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh_binary', thresh_binary)
_, thresh_trunc = cv2.threshold(img, 79, 255, cv2.THRESH_TRUNC)
cv2.imshow('thresh_trunc', thresh_trunc)
_, thresh_tozero = cv2.threshold(img, 79, 255, cv2.THRESH_TOZERO)
cv2.imshow('thresh_tozero', thresh_tozero)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(thresh, contours, -1, (0, 255, 0))
cv2.imshow('Contours', thresh)
interrupt = cv2.waitKey(0) & 0xFF
if interrupt == 27:
    cv2.destroyAllWindows()