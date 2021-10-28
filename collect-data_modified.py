import cv2
import os

if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/train/6")
    os.makedirs("data/train/7")
    os.makedirs("data/train/8")
    os.makedirs("data/train/9")
    
 
mode = 'train'
directory = 'data/'+mode+'/'

# url = '<YOUR IP ADDRESS>/video'
# cap=cv2.VideoCapture(url)

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    cv2.putText(frame, "subha-18", (int(0.35*frame.shape[1]),int(0.25*frame.shape[1]) ), cv2.FONT_HERSHEY_SIMPLEX, 1, (147,20,255), 3)

    count = {'zero': len(os.listdir(directory+"/0")),
             'one(index)': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'one_thumb': len(os.listdir(directory+"/6")),
             'two_2nd_4th': len(os.listdir(directory+"/7")),
             'three_3rd_4th_5th': len(os.listdir(directory+"/8")),
             'blank': len(os.listdir(directory+"/9"))
             }
    
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 1)
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,153,51), 1)
    cv2.putText(frame, "ONE : "+str(count['one(index)']), (10, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (204,102,0), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 160), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,102,102), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,51,51), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (204,0,0), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (153,0,76), 1)
    cv2.putText(frame, "one_thumb(6) : "+str(count['one_thumb']), (10, 240), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (153,0,76), 1)
    cv2.putText(frame, "two_2nd_4th(7) : "+str(count['two_2nd_4th']), (10, 260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (153,0,76), 1)
    cv2.putText(frame, "three_3rd_4th_5th(8) : "+str(count['three_3rd_4th_5th']), (10, 280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (153,0,76), 1)
    cv2.putText(frame, "blank(9): "+str(count['blank']), (10, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (153,0,76), 1)

    
    
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,3)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (300, 300)) 
    cv2.putText(frame, "R.O.I", (int(0.75*frame.shape[1]),int(0.55*frame.shape[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,225,0), 3)
    cv2.imshow("Frame", frame)
    
   


    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.GaussianBlur(roi, (5, 5), 0)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
    cv2.imshow("ROI", roi)


    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one(index)'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['one_thumb'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['two_2nd_4th'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['three_3rd_4th_5th'])+'.jpg', roi)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['blank'])+'.jpg', roi)

    
    
cap.release()
cv2.destroyAllWindows()
