import cv2

(width, height) = (130, 100)

# url = '<YOUR IP ADDRESS>/video'
# cap=cv2.VideoCapture(url)


cap=cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, img = cap.read()
    img=cv2.flip(img, 1)
    cv2.rectangle(img, (20, 20), (250, 250), (255, 0, 0), 3)
    #cv2.imshow("RGB Output", img)
    img1 = img[20:250,20:250]       
    imCopy1 = img1.copy()
    imCopy2 = img1.copy()
    imCopy3 = img1.copy()
    imCopy4 = img1.copy()
    imCopy5 = img1.copy()
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    hand_resize = cv2.resize(thresh1, (width, height))
    #cv2.imshow("Threshold1", thresh1)
    ret, thresh2 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    hand_resize = cv2.resize(thresh2, (width, height))
    #cv2.imshow("Threshold2", thresh2)
    ret, thresh3 = cv2.threshold(blur, 10, 255, cv2.THRESH_TRIANGLE)
    hand_resize = cv2.resize(thresh3, (width, height))
    #cv2.imshow("Threshold3", thresh3)
    contours1, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy1, contours1, -1, (0, 255, 0))
    cv2.imshow('Contours1', imCopy1)
    contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy2, contours2, -1, (0, 255, 0))
    cv2.imshow('Contours2', imCopy2)
    contours3, hierarchy = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy3, contours3, -1, (0, 255, 0))
    cv2.imshow('Contours3', imCopy3)
    contours4, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy4, contours4, -1, (0, 255, 0))
    cv2.imshow('Contours4', imCopy4)
    k = cv2.waitKey(10) & 0xFF 
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
