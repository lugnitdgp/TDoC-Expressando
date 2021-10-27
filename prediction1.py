from keras.models import model_from_json
import operator
import cv2

json_file = open("model-bw1.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("model-bw1.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0) 

categories = {0: "best of luck", 1: "call", 2: "hello", 3: "peace" , 4: "yo man!"}

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    cv2.putText(frame, "Expressando - TDOC 2021", (175, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,0), 3)
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,255,255) ,3)
    roi = frame[y1:y2, x1:x2]

    roi = cv2.resize(roi, (64, 64)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame, "R.O.I", (440, 350), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,225,0), 3)

    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", test_image)

    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    prediction = {'best of luck': result[0][0], 
                  'call': result[0][1], 
                  'hello': result[0][2],
                  'peace': result[0][3],
                  'yo man!': result[0][4]} 
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True) 
    cv2.putText(frame, "PREDICTION:", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(frame, prediction[0][0], (80, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)    
    cv2.imshow("Frame", frame)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
