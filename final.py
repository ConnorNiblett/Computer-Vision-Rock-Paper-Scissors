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
user_choice = ''

message = ''
while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0]= normalized_image
    prediction = model.predict(data)
    if not started:
        message = 'Press a to start'
    if cv2.waitKey(33) == ord('a'):
        if not started:
            counter = time.time()
            started = True
            countdown = True

    if started:
        print('elapsed = ', elapsed)
        print('counter = ', counter)
        print('time.time() - counter = ', time.time() - counter)
        elapsed = 5 - (time.time() - counter)
        if elapsed <= -5:
                countdown = False
                prediction_max = np.argmax(prediction)
                if prediction_max == [0]:
                    user_choice = 'Rock'
                elif prediction_max == [1]:
                    user_choice = 'Paper'
                elif prediction_max == [2]:
                     user_choice = 'Scissors'
                computer = random.choice(['Rock', 'Paper', 'Scissors'])
                message = 'Press n to play the next round'
                if cv2.waitKey(33) == ord('n'):
                    started = False
                    elapsed = 0
        
        if elapsed <=0:
            message = f'You showed {user_choice}, and the computer showed {computer}. '
            if prediction_max == [0]:
                if computer == 'Rock':
                    message += "It's a draw"
                elif computer == 'Paper':
                    message += 'Sorry, you lose'
                elif computer == 'Scissors':
                    message += 'Great, you win!'
            elif prediction_max == [1]:
                if computer == 'Rock':
                    message += 'Great, you win'
                elif computer == 'Paper':
                    message += "It's a draw"
                elif computer == 'Scissors':
                    message += 'Sorry, you lose'
            elif prediction_max == [2]:
                if computer == 'Rock':
                    message += 'Sorry, you lose'
                elif computer == 'Paper':
                    message += 'Great, you win!'
                elif computer == 'Scissors':
                    message += "It's a draw"
            else:
                continue
        if countdown:
            message = f'Show your hand in {int(elapsed)} seconds'

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

    
    