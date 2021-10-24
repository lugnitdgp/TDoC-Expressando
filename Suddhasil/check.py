import cv2
img = cv2.imread('SampleImage.jpg')
img2= cv2.resize(img, (300,250))
cv2.imshow("Original Image",img2)
imCopy=img2.copy()
gray=cv2.cvtColor(img2 ,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Blur Image",blur)

ret, thresh1= cv2.threshold(blur,10,225,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Thresh_bin_inv", thresh1)

ret, thresh2= cv2.threshold(blur,10,225,cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
cv2.imshow("Thresh_tozero", thresh2)

ret, thresh3= cv2.threshold(blur,10,225,cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
cv2.imshow("Thresh_tozero_inv", thresh3)

ret, thresh4= cv2.threshold(blur,10,225,cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
cv2.imshow("Thresh_trunc", thresh4)

ret, thresh5= cv2.threshold(blur,10,225,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Thresh_bin", thresh5)

contours, hierarchy= cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy, contours, -1, (0,255,0))
cv2.imshow('Tree Contour',imCopy)

contours, hierarchy= cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy, contours, -1, (0,255,0))
cv2.imshow('List Contour',imCopy)

interrupt=cv2.waitKey(0) & 0xFF
if interrupt==27:
    cv2.destroyAllWindows()
