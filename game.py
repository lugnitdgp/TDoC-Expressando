from keras.models import load_model
import cv2
import numpy as np
from random import choice

game_moves = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

def mapper(val):
    return game_moves[val]

def calculate_winner(move1, move2):
    if move1 == move2:
        return "Tie"

    if move1 == "rock":
        if move2 == "scissors":
            return "User"
        if move2 == "paper":
            return "Computer"

    if move1 == "paper":
        if move2 == "rock":
            return "User"
        if move2 == "scissors":
            return "Computer"

    if move1 == "scissors":
        if move2 == "paper":
            return "User"
        if move2 == "rock":
            return "Computer"


model = load_model("model.h5")

cap = cv2.VideoCapture(0)
cap.set(3, 1280) # Property for width
cap.set(4, 720) # Property for height

prev_move = None

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # User rectangle
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    # Computer rectangle
    cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2)

    # Extraction
    roi = frame[100:500, 100:500]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 1)
    roi = cv2.resize(roi, (64, 64)) 
    roi = roi.reshape(64, 64, 1)

    # Prediction
    pred = model.predict(np.array([roi]))
    move_code = np.argmax(pred[0])
    user_move_name = mapper(move_code)

    # Winner prediction
    if prev_move != user_move_name:
        if user_move_name != "none":
            computer_move_name = choice(['rock', 'paper', 'scissors'])
            winner = calculate_winner(user_move_name, computer_move_name)
        else:
            computer_move_name = "none"
            winner = "Waiting..."
    prev_move = user_move_name

    # Display text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Your Move: " + user_move_name,
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Computer's Move: " + computer_move_name,
                (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Winner: " + winner,
                (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)

    if computer_move_name != "none":
        icon = cv2.imread(
            "images/{}.png".format(computer_move_name))
        icon = cv2.resize(icon, (400, 400))
        frame[100:500, 800:1200] = icon
    else:
        icon = cv2.imread("images/none.png")
        icon = cv2.resize(icon, (400, 400))
        frame[100:500, 800:1200] = icon

    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()