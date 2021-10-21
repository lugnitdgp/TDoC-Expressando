import cv2

img = cv2.imread('pixel.jpg')

while(True):
    
    resized = cv2.resize(img, (564, 350))
    cv2.imshow("Original", resized)
    imcopy = resized.copy()

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret2, thresh2 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    ret3, thresh3 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imcopy, contours, -1, (0, 255, 0))

    cv2.imshow('RETR_EXTERNAL', imcopy)
    cv2.imshow('gray',gray)
    cv2.imshow('THRESH_BINARY_INV', thresh)
    cv2.imshow("THRESH_TOZERO", thresh2)
    cv2.imshow("THRESH_TOZERO_INV", thresh3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
