import cv2

(width,height) = (130,100)

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # will return the mirror view
    cv2.rectangle(img, (20, 20), (250,250), (255, 0, 0), 2) #BGR
    cv2.imshow("BGR Output", img)
    
    img1 = img[20:250, 20:250] # Extraction
    imCopy = img1.copy() #Copy of the extraction
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    cv2.imshow("Blur",blur)

    ret, thresh1 = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) #0 to 255   
    hand_resize = cv2.resize(thresh1, (width,height))
    cv2.imshow("Threshold", thresh1)



    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #contour tells us the minimum nuber of edges required to express a shape
    cv2.drawContours(imCopy, contours, -1, (0, 255, 0))
    cv2.imshow('RETR TREE', imCopy)

    k = 0xFF & cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

# import cv2

# (width, height) = (130, 100)

# # url = '<YOUR IP ADDRESS>/video'
# # cap=cv2.VideoCapture(url)


# cap=cv2.VideoCapture(0)

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
