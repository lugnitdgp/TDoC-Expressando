import cv2
import os

if not os.path.exists("data"): #True
    os.makedirs("data")
    os.makedirs("data/train") 
    os.makedirs("data/test")
    os.makedirs("data/train/rock") 
    os.makedirs("data/train/paper")
    os.makedirs("data/train/scissor")
    os.makedirs("data/train/none")
    os.makedirs("data/test/rock")
    os.makedirs("data/test/paper")
    os.makedirs("data/test/scissor")
    os.makedirs("data/test/none")
    
 
mode = 'TRAIN' 
directory = 'data/'+mode+'/' #data/train/

cap=cv2.VideoCapture(0)
cap.set(3, 1280) # 3 - PROPERTY index for WIDTH
cap.set(4, 720) # 4 - PROPERTY index for HEIGHT

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    cv2.putText(frame, "GitHub: Daksh777", (900, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)

    count = {'rock': len(os.listdir(directory+"/rock")), 
             'paper': len(os.listdir(directory+"/paper")),
             'scissor': len(os.listdir(directory+"/scissor")),
             'none': len(os.listdir(directory+"/none"))} 
    
    cv2.putText(frame, "MODE : "+ mode, (900, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT:", (900, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "ROCK : "+str(count['rock']), (900, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "PAPER : "+str(count['paper']), (900, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "SCISSORS : "+str(count['scissor']), (900, 160), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "NONE : "+str(count['none']), (900, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    roi = frame[100:500, 100:500]
    roi = cv2.resize(roi, (64, 64))
    cv2.putText(frame, "R.O.I", (270, 550), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,225,0), 2)
    cv2.imshow("Frame", frame)

    
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 1)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10) 
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'rock/'+str(count['rock'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'paper/'+str(count['paper'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'scissor/'+str(count['scissor'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'none/'+str(count['none'])+'.jpg', roi)
    
cap.release()
cv2.destroyAllWindows()