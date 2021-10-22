import cv2

(width, height) = (250,250)

img = cv2.imread('img01.jpg')
img = cv2.resize(img, (width, height))
cv2.imshow("Original", img)

# img1 = img[20:250,20:250]       
imCopy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 10)
ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, thresh2 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret, thresh4 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
ret, thresh5 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
ret, thresh6 = cv2.threshold(blur, 10, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
# ret9, thresh9 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
# ret10, thresh10 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)

# hand_resize = cv2.resize(thresh1, (width, height))
cv2.imshow("Thresh_Bin", thresh1)
cv2.imshow("Thresh_Bin_Inv", thresh2)
cv2.imshow("Thresh_TZ", thresh4)
cv2.imshow("Thresh_TZ_Inv", thresh5)
cv2.imshow("Thresh_Trunc", thresh6)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)
# cv2.imshow("A_Thresh_TZ", thresh9)
# cv2.imshow("A_Thresh_TZ", thresh10)


contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy, contours1, -1, (0, 255, 0))
cv2.imshow('Cont_Tree', imCopy)

contours2, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(blur, contours2, -1, (255, 0, 0))
cv2.imshow('Cont_CC', imCopy)

contours3, hierarchy = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy, contours3, 0, (0, 0, 255))
cv2.imshow('Cont_List', imCopy)

interrupt = cv2.waitKey(0) & 0xFF
if interrupt == ord('q'):
    cv2.destroyAllWindows()

