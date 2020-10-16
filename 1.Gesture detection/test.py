from keras.models import load_model
import cv2
import numpy as np
from random import choice


from threading import Thread
import pyttsx3
user_move_name="begin"
def myfunc():
  engine = pyttsx3.init()
  engine.say(user_move_name)
  engine.runAndWait()



REV_CLASS_MAP = {
    0: "0",
    1: "1",
    2: "2",
    3:"3",
    4:"4",
    5:"5",
    6: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]



model = load_model("Gesture_Detect_0.h5")

cap = cv2.VideoCapture(0)

prev_move = None
t = Thread(target=myfunc())
t.start()
while True:
    ret, frame = cap.read()
    print(frame.shape)
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (0, 0), (320, 240), (255, 0, 0), 2)

    # extract the region of image within the user rectangle
    roi = frame[ 0:227,0:227]

    cv2.imshow('roi',roi)
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))

    # predict the move made
    pred = model.predict(np.array([img]))
    move_code = np.argmax(pred[0])
    user_move_name = mapper(move_code)
    prev_move = user_move_name

    # display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Your Move: " + user_move_name,
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

##    # speak the gesture detected
##    if user_move_name !="none":

	
    cv2.imshow("frame", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
