from ast import Return
from webbrowser import get
import cv2
from keras.models import load_model
import numpy as np
import itertools
import random
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
prediction = model.predict(data)
started = False
next_round = True
countdown = False
counter = 0
elapsed = 0 
round_time = 0

UserScore = 0
ComputerScore = 0

message = ''
t_0 = time.time()
while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
            
    cv2.imshow('frame', frame)

    if cv2.waitKey(50) == ord('a'):
        if not started:
            counter = time.time()
            started = True
            countdown = True

    if started:
        elapsed = 5 - (time.time() - counter)
        if elapsed <= -4:
            message = 'Press n to play next round'
            if cv2.waitKey(50) == ord('n'):
                started = False
                elapsed = 0

    elif elapsed <= 0:
        countdown = False    
    possible_actions = ["Rock", "Paper", "Scissors"]
    user_action = prediction 
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    if prediction [0][0] > 0.5:
        user_action = "Rock"
        print ("Rock")
    if prediction [0][1] > 0.5:
        user_action = "Paper"
        print ("Paper")
    if prediction [0][2] > 0.5:
        user_action = "Scissors"
        print ("Scissors")
    else:
        user_action = "Nothing"
        print ("Nothing")
    print (f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print ("Rock smashes Scissors! You win!")
            UserScore += 1
        else:
            print ("Paper covers Rock! You lose.")
            ComputerScore += 1
    elif user_action == "Paper":
        if computer_action == "Rock":
            print ("Paper covers Rock! You win!")
            UserScore += 1
        else:
            print ("Scissors cut Paper! You lose.")
            ComputerScore += 1
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print ("Scissors cut Paper! You win!")
            UserScore += 1
        else:
            print ("Rock smashes Scissors! You lose.")
            ComputerScore += 1

    print (UserScore)
    print (ComputerScore)
    if UserScore < ComputerScore:
        print ("You lose!")
    elif UserScore == ComputerScore:
        print ("Tie game...")
    else:
        print ("You win!")

    

    # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()