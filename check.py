import cv2

img = cv2.imread('download.jpeg')
img2 = cv2.resize(img, (200,400))
cv2.imshow("Image", img2)

(width, height) = (200, 200)

cap=cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, img = cap.read()
    img=cv2.flip(img, 1)
    cv2.rectangle(img, (150, 100), (500, 450), (255, 0, 0), 3)
    cv2.imshow("RGB Output", img)
    img1 = img[150:500,150:500]
    imCopy = img1.copy()
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    cv2.imshow("B&W", gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("Blur", blur)
    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    hand_resize = cv2.resize(thresh1, (width, height))
    cv2.imshow("Threshold", thresh1)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
    cv2.imshow('Draw Contours', imCopy)
    k = 0xFF & cv2.waitKey(10)
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
