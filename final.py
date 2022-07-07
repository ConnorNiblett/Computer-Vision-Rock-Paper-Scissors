from ssl import get_protocol_name
import cv2
from keras.models import load_model
import numpy as np
import time
import random
from time import sleep
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
started = False
next_round = True
countdown = False
counter = 0
elapsed = 0
round_time = 0
UserScore = 0
ComputerScore = 0
global user_choice 
global prediction_max
global computer
global get_prediction
global get_winner
user_choice = ''
winner_message = ''

message = ''
while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0]= normalized_image
    prediction = model.predict(data)
    if started == False:
        message = 'Press a to start'
    if cv2.waitKey(33) == ord('a'):
            started = True
            counter = time.time()
            countdown = True
            get_winner = False

    if countdown:
        message = f'Show your hand in { 5- int(elapsed)} seconds'

    if started:
        print('elapsed = ', elapsed)
        print('counter = ', counter)
        print('time.time() - counter = ',(time.time() - counter))
        elapsed = (time.time() - counter)
        if elapsed >= 5 :
            countdown = False
            if get_winner == False:
                prediction_max = np.argmax(prediction)
                if prediction_max == [0]:
                    user_choice = 'Rock'
                elif prediction_max == [1]:
                    user_choice = 'Paper'
                elif prediction_max == [2]:
                    user_choice = 'Scissors'
                computer = random.choice(['Rock', 'Paper', 'Scissors'])

                if prediction_max == [0]:
                    if computer == 'Rock':
                        message = "It's a draw"
                    elif computer == 'Paper':
                        message = 'Sorry, you lose'
                    elif computer == 'Scissors':
                        message = 'Great, you win!'
                elif prediction_max == [1]:
                    if computer == 'Rock':
                        message = 'Great, you win!'
                    elif computer == 'Paper':
                        message = "It's a draw"
                    elif computer == 'Scissors':
                        message = 'Sorry, you lose'
                elif prediction_max == [2]:
                    if computer == 'Rock':
                        message = 'Sorry, you lose'
                    elif computer == 'Paper':
                        message = 'Great, you win!'
                    elif computer == 'Scissors':
                        message = "It's a draw"

                winner_message = f'You showed {user_choice}, and the computer showed {computer}. '
    
                if message == 'Great, you win!':
                    UserScore += 1
                    print(UserScore)
                    get_winner = True
                elif message == 'Sorry, you lose':
                    ComputerScore += 1
                    print(ComputerScore)
                    get_winner = True
                else:
                    get_winner = True
                    continue
                
            if UserScore == 3:
                print("You win")
                break
            if ComputerScore == 3:
                print("You Lose")
                break

            round_restart = 'Hold n to play the next round' 
            cv2.putText(frame, round_restart, (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)    
            cv2.putText(frame, winner_message, (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)      
            if cv2.waitKey(50) == ord('n'):
                started = False
                elapsed = 0   

    print(UserScore, ComputerScore)
    print(UserScore, ComputerScore)
    print(UserScore, ComputerScore)
    print(UserScore, ComputerScore)
      
    # cv2.putText(frame, message, (150, 150), fontFace=)
    cv2.putText(frame, message, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    cv2.imshow('frame', frame)
    # Press q to close the window
    # print(prediction)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

    
    
    
    