import cv2

while (1):
    
    img = cv2.imread('download.jpg')
    cv2.imshow("actual img", img)   
    
    imgCopy = []
    for ii in range(5):
        imgCopy.append(img.copy())
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("blur", blur)

    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow("Threshold", thresh1)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgCopy[0], contours, -1, (0, 255, 0))
    cv2.imshow('RETR_TREE', imgCopy[0])

    contours1, comp = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgCopy[1], contours1, -1, (0, 255, 0))
    cv2.imshow('RETR_CCOMP', imgCopy[1])

    contours2, ext = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgCopy[2], contours2, -1, (0, 255, 0))
    cv2.imshow('RETR_EXTERNAL', imgCopy[2])

    contours3, lists = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgCopy[3], contours3, -1, (0, 255, 0))
    cv2.imshow('RETR_LIST', imgCopy[3])

    k = 0xFF & cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
