import cv2

(width, height) = (200, 200)

img = cv2.imread('abc.jpg')
cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("blur", blur)

ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
hand_resize = cv2.resize(thresh1, (width, height))
cv2.imshow("Thresh binary inverse", thresh1)

ret, thresh2 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
hand_resize = cv2.resize(thresh2, (width, height))
cv2.imshow("Thresh tozero", thresh2)

ret, thresh3 = cv2.threshold(blur, 10, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
hand_resize = cv2.resize(thresh3, (width, height))
cv2.imshow("Thresh trunc", thresh3)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0))
cv2.imshow('Contours- tree', img)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255))
cv2.imshow('Contour- list', img)

interrupt = cv2.waitKey(0) & 0xFF
if interrupt == 27:
  cv2.destroyAllWindows()
