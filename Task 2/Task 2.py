# Task 2

# Modules Imported
import cv2
import os
import numpy as np

# Checking if the said folders are already present there in the Python file directory or not,
# and if it's not there then the said folders are created in the same directory.
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")

mode = 'train'
directory = 'data/' + mode + '/'

# Capturing video feed from the first web cam connected to the system
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # flipping the frame for better visual

    # Putting text onto the frame captured
    cv2.putText(frame, "SHIRSENDU KONER - TDOC 2021", (175, 460),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 150, 255), 2)

    # Creating a dictionary to count the number of images for each finger image captured
    count = {'zero': len(os.listdir(directory + "/0")),
             'one': len(os.listdir(directory + "/1")),
             'two': len(os.listdir(directory + "/2")),
             'three': len(os.listdir(directory + "/3")),
             'four': len(os.listdir(directory + "/4")),
             'five': len(os.listdir(directory + "/5"))}

    # Putting Labels onto the Frame directly
    cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225, 255, 255), 1)
    cv2.putText(frame, "ZERO  : " + str(count['zero']), (10, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)
    cv2.putText(frame, "ONE   : " + str(count['one']), (10, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)
    cv2.putText(frame, "TWO   : " + str(count['two']), (10, 160), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)
    cv2.putText(frame, "THREE : " + str(count['three']), (10, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)
    cv2.putText(frame, "FOUR  : " + str(count['four']), (10, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)
    cv2.putText(frame, "FIVE   : " + str(count['five']), (10, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)

    # Separating the Region of Interest for our work
    # (x1, y1) and (x2, y2) are the two diagonal corner points or coordinates of the rectangle drawn
    x1 = int(0.5 * frame.shape[1])  # frame.shape[1] gives the width of the frame
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (0, 0, 255), 3)  # Drawing a rectangle onto the frame
    roi = frame[y1:y2, x1:x2]  # slicing a part of the frame
    roi = cv2.resize(roi, (200, 200))  # resizing the sliced part
    cv2.putText(frame, "R.O.I", (440, 350), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (50, 225, 150), 2)
    cv2.imshow("Frame", frame)

    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  # Changing Colour Space of our R.O.I
    # i.e. color frame -> black and white frame
    # rev, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    roi = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
    cv2.imshow("ROI", roi)

    # Images are captured and stored when respective keys are pressed
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # 27 refers to the ESC key on our keyboard
        break
    if interrupt & 0xFF == ord('0'):  # when 0 is pressed
        cv2.imwrite(directory + '0/' + str(count['zero']) + '.jpg', roi)
    if interrupt & 0xFF == ord('1'):  # when 1 is pressed
        cv2.imwrite(directory + '1/' + str(count['one']) + '.jpg', roi)
    if interrupt & 0xFF == ord('2'):  # when 2 is pressed
        cv2.imwrite(directory + '2/' + str(count['two']) + '.jpg', roi)
    if interrupt & 0xFF == ord('3'):  # when 3 is pressed
        cv2.imwrite(directory + '3/' + str(count['three']) + '.jpg', roi)
    if interrupt & 0xFF == ord('4'):  # when 4 is pressed
        cv2.imwrite(directory + '4/' + str(count['four']) + '.jpg', roi)
    if interrupt & 0xFF == ord('5'):  # when 5 is pressed
        cv2.imwrite(directory + '5/' + str(count['five']) + '.jpg', roi)

cap.release()
cv2.destroyAllWindows()
