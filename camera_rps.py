import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)


    
    
    # get prediction from camera
    # use camera prediction as input to game
    # get random computer choice
    # compare user and computer choice
    # get winner of comparison
    # Update score
    #if q is pressed quit the game
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
def get_prediction():
    prediction = model.predict(data)
    return prediction
def get_computer_choice(choices):
    np.random.choice(choices)
def get_user_choice():
    # get prediction
    # find out what prediction is greatest
    # set greatest prediction equal to user choice
    if prediction[0][1] > 0.5:
        user_choice = "Rock"
def get_winner():
    # get user choice
    # get a computer choice
    # compare the two
    # get winner
if user_choice == "Scissors":
    
