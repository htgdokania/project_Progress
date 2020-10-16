# import pyttsx3
# engine = pyttsx3.init()
# engine.speak("hello")

# #engine.say("I will speak this text")
# #engine.runAndWait()

from threading import Thread
import pyttsx3

def myfunc():
  engine = pyttsx3.init()
  engine.say("ok")
  engine.runAndWait()

t = Thread(target=myfunc)
t.start()