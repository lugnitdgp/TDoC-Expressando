# import cv2
# (width, height) = (130, 100)
# cap = cv2.VideoCapture(0)
# while (cap.isOpened()):
#     ret, img = cap.read()
#     img=cv2.flip(img, 1)
#     cv2.rectangle(img, (20, 20), (250, 250), (255, 0, 0), 3)
#     cv2.imshow("RGB Output", img)
#     img1 = img[20:250,20:250]
#     imCopy = img1.copy()
#     gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#     hand_resize = cv2.resize(thresh1, (width, height))
#     cv2.imshow("Threshold", thresh1)
#     contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
#     cv2.imshow('Draw Contours', imCopy)

#     k = 0xFF & cv2.waitKey(10)
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

# STATIC IMAGES INPUT

import cv2
img = cv2.imread('img.jpg')
cv2.imshow("Original Image", img)
img1 = cv2.resize(img, (300, 300))
cv2.imshow("Resized image", img1)
# ret, img = cap.read()
img2=cv2.flip(img1, 1)
cv2.imshow("Flipped image", img2)
cv2.rectangle(img2, (20, 20), (250, 250), (255, 0, 0), 3)
cv2.imshow("RGB Output", img2)
img3 = img2[20:250,20:250]
imCopy = img3.copy()
gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",gray)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("GaussianBlur",blur)
ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
hand_resize = cv2.resize(thresh1, (500, 400))
cv2.imshow("Threshold", thresh1)
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy, contours, -1, (0, 0, 0))
cv2.imshow('Draw Contours', imCopy)
# cv2.imshow("Image", img2)
interrupt = cv2.waitKey(0) & 0xFF
if interrupt == 27:
    cv2.destroyAllWindows()
