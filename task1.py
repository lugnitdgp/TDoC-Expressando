import cv2

#(width, height) = (130, 100)

# url = '<YOUR IP ADDRESS>/video'
# cap=cv2.VideoCapture(url)


cap=cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, img = cap.read()
    img=cv2.flip(img, 1)
    cv2.rectangle(img, (20, 20), (250, 250), (255,0,0), 4, cv2.LINE_AA)
    cv2.imshow("RGB Output", img)
    img1 = img[20:250,20:250]       
    imCopy = img1.copy()
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (35, 35), 0)

    cv2.imshow("Grayscale",gray)
    cv2.imshow('Blur', blur)

    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #hand_resize = cv2.resize(thresh1, (width, height))
    cv2.imshow("Thresh binary ", thresh1)
    
    ret, thresh2 = cv2.threshold(blur, 10, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    cv2.imshow("Tozero ", thresh2)

    ret, thresh3 = cv2.threshold(blur, 10, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    cv2.imshow("Trunc ", thresh3)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
    cv2.imshow('Contours_tree', imCopy)
    
    imCopy3 = img1.copy()
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imCopy3, contours, -1, (0, 255, 0))
    cv2.imshow('Contours_list', imCopy3)

    imCopy2 = img1.copy()
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imCopy2, contours, -1, (0, 255, 0))
    cv2.imshow('Contours_external', imCopy2)



    k = 0xFF & cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
