import cv2
import os

if not os.path.exists("data1"):
    os.makedirs("data1")
    os.makedirs("data1/train")
    os.makedirs("data1/train/hello")
    os.makedirs("data1/train/peace")
    os.makedirs("data1/train/best of luck")
    os.makedirs("data1/train/call")
    os.makedirs("data1/train/yo man!")
    
    
 
mode = 'train'
directory = 'data1/'+mode+'/'

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    cv2.putText(frame, "sayantani-12", (150, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 3)

    count = {'hello': len(os.listdir(directory+"hello")),
             'peace': len(os.listdir(directory+"peace")),
             'best of luck': len(os.listdir(directory+"best of luck")),
             'call': len(os.listdir(directory+"call")),
             'yo': len(os.listdir(directory+"yo man!"))}
    
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "hell0 : "+str(count['hello']), (10, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "peace : "+str(count['peace']), (10, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "best of luck : "+str(count['best of luck']), (10, 160), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "call : "+str(count['call']), (10, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "yo! : "+str(count['yo']), (10, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    
    
    
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,50,255) ,3)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (200, 200)) 
    cv2.putText(frame, "R.O.I", (440, 350), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100,225,50), 3)
    cv2.imshow("Frame", frame)
    
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)


    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'hello/'+str(count['hello'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'peace/'+str(count['peace'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'best of luck/'+str(count['best of luck'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'call/'+str(count['call'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'yo man!/'+str(count['yo'])+'.jpg', roi)
    
    
cap.release()
cv2.destroyAllWindows()
