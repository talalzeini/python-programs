# pip install pyttsx3
import pyttsx3 as pyttsx3

engine = pyttsx3.init()
engine.say("Meow")
print("This program works.")
engine.runAndWait()