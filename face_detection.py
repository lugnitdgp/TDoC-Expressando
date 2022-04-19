# FACE DETECTION FOR VIDEO FROM WEBCAM
# if you are importing any photo comment out this part upto cap.release()
import cv2
# Doing by importing a cascade
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayscale, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('img', frame)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()

#------------------------------------------------------------------------------#

# FACE DETECTION FROM PHOTOS
# if you want to get output from videos via webcam comment out upto cv2.waitkey()
# import cv2
# # Doing by importinfg the cascade
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img2 = cv2.imread('img1.jpg') #since i am taking input from img1.jpg
# img = cv2.resize(img2, (1300, 700))
# grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = cascade.detectMultiScale(grayscale, 1.1, 3)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cv2.imshow('img', img)
# cv2.waitKey()

#------------------------------------------------------------------------------#