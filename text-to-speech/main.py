import pyttsx3 as pyttsx3
# Install pyttsx3 using the following commands
# pip install pyttsx3
# or
# python3 -m pip install pyttsx3

engine = pyttsx3.init()
engine.say("This program works.")
print("This program works.")
engine.runAndWait()
