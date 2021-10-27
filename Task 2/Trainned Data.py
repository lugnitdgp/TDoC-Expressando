import cv2
import os

if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/train/0 front")
    os.makedirs("data/train/0 back")
    os.makedirs("data/train/1 front")
    os.makedirs("data/train/1 back")
    os.makedirs("data/train/2 front")
    os.makedirs("data/train/2 back")
    os.makedirs("data/train/3 front")
    os.makedirs("data/train/3 back")
    os.makedirs("data/train/4 front")
    os.makedirs("data/train/4 back")
    os.makedirs("data/train/5 front")
    os.makedirs("data/train/5 back")
    
 
mode = 'train'
directory = 'data/'+mode+'/'

# url = '<YOUR IP ADDRESS>/video'
# cap=cv2.VideoCapture(url)

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    cv2.putText(frame, "SHOW THE NUMBER OF FINGERS FOR OUTPUT", (175, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 3)

    count = {'zero-front': len(os.listdir(directory+"/0 front")),
             'zero-back': len(os.listdir(directory+"/0 back")),
             'one-front': len(os.listdir(directory+"/1 front")),
             'one-back': len(os.listdir(directory+"/1 back")),
             'two-front': len(os.listdir(directory+"/2 front")),
             'two-back': len(os.listdir(directory+"/2 back")),
             'three-front': len(os.listdir(directory+"/3 front")),
             'three-back': len(os.listdir(directory+"/3 back")),
             'four-front': len(os.listdir(directory+"/4 front")),
             'four-back': len(os.listdir(directory+"/4 back")),
             'five-front': len(os.listdir(directory+"/5 front")),
             'five-back': len(os.listdir(directory+"/5 back"))}
    
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "ZERO - FRONT : "+str(count['zero-front']), (10, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "ZERO - BACK : "+str(count['zero-back']), (10, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "ONE - FRONT : "+str(count['one-front']), (10, 160), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "ONE - BACK : "+str(count['one-back']), (10, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "TWO - FRONT : "+str(count['two-front']), (10, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "TWO - BACK : "+str(count['two-back']), (10, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "THREE - FRONT : "+str(count['three-front']), (10, 240), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "THREE - BACK : "+str(count['three-back']), (10, 260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "FOUR - FRONT : "+str(count['four-front']), (10, 280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "FOUR - BACK : "+str(count['four-back']), (10, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "FIVE - FRONT : "+str(count['five-front']), (10, 320), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "FIVE - BACK : "+str(count['five-back']), (10, 340), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    
    
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,3)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (200, 200)) 
    cv2.putText(frame, "R.O.I", (440, 350), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,225,0), 3)
    cv2.imshow("Frame", frame)
    
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)


    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0 front/'+str(count['zero-front'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'0 back/'+str(count['zero-back'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'1 front/'+str(count['one-front'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'1 back/'+str(count['one-back'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'2 front/'+str(count['two-front'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'2 back/'+str(count['two-back'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'3 front/'+str(count['three-front'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'3 back/'+str(count['three-back'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'4 front/'+str(count['four-front'])+'.jpg', roi)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'4 back/'+str(count['four-back'])+'.jpg', roi)
    if interrupt & 0xFF == ord('+'):
        cv2.imwrite(directory+'5 front/'+str(count['five-front'])+'.jpg', roi)
    if interrupt & 0xFF == ord('-'):
        cv2.imwrite(directory+'5 back/'+str(count['five-back'])+'.jpg', roi)
    
cap.release()
cv2.destroyAllWindows()
