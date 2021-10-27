import cv2

img = cv2.imread('road.jpeg') #Static Image
cv2.resize(img, (250,250))
cv2.imshow("source",img)
imCopy = img.copy() #Copy of the extraction

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("BLURRED",blur)

blur = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("BLURRED Gray",blur)

ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) #0 to 255   
cv2.imshow("BINARY INVERSE", thresh1)

ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #0 to 255   
cv2.imshow("BINARY", thresh1)

ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU) #0 to 255   
cv2.imshow("Thresh_ToZero", thresh1)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #contour tells us the minimum nuber of edges required to express a shape
cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
cv2.imshow('RETR TREE', imCopy)

interrupt = cv2.waitKey(0) & 0xFF #Stopping Unicode Value
if interrupt == ord('q'): #ord returns the Unicode of 'q'
    cv2.destroyAllWindows()