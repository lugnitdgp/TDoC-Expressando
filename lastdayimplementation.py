import cv2
 

image = cv2.imread('emma3.jpg')
cv2.imshow('Original', image)

 

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Grayscale', gray_image)


ret, thresh1= cv2.threshold(gray_image,140,255,cv2.THRESH_BINARY)

cv2.imshow("Binary thresh",thresh1)

contours,heirarchy = cv2.findContours(image=thresh1,mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_SIMPLE)
image_copy=image.copy()
cv2.drawContours(image=image_copy,contours=contours,contourIdx=-1,color=(255,0,120),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow("Contour using list",image_copy)

cv2.waitKey(0)

cv2.destroyAllWindows()