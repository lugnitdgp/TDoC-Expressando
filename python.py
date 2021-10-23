import cv2



# url = '<YOUR IP ADDRESS>/video'
# cap=cv2.VideoCapture(url)





img =cv2.imread('img.jpg')   
cv2.imshow("Original",img)  
imCopy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale",gray)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
ret, thresh1 = cv2.threshold(
    blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
hand_resize = cv2.resize(thresh1, (130, 100))
cv2.imshow("Threshold To Zero", thresh1)

contours, hierarchy = cv2.findContours(
    thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
cv2.imshow('Draw Contours CComp', imCopy)

k = 0xFF & cv2.waitKey(0) 
if k == 27:

 cv2.destroyAllWindows()
