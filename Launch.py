import pyttsx3
import os
import time
import speech_recognition as sr
import random
from quotes import ql

# global vars for name, current hour, voiceID, and voice Rate
NAME = "Rohan"
time = int(time.strftime('%H'))
voiceID = 28 # Other voice ID's -> SHm: 11, SAf: 17, Brf: 28 , YTm : 7, USf: 33, JPf: 18, Spf: 26
RATE = 200

#Applications
Apps = {
    "lol": {"appName": "League of Legends", "Path": "/Applications/League\ of\ Legends.app/"},
    "chrome": {"appName": "Google Chrome", "Path": "/Applications/Google\ Chrome.app/"},
    "fire": {"appName": "Fire Fox", "Path": "/Applications/Firefox.app/"}
    }

myKeys = Apps.keys()

#initializing libraries
r = sr.Recognizer()

def setUpEngine(engine):
	voices = engine.getProperty('voices')
	engine.setProperty("rate", RATE)
	engine.setProperty('voice', voices[voiceID].id)

def SpeakText(command):
	engine = pyttsx3.init()
	setUpEngine(engine)
	engine.say(command)
	engine.runAndWait()

# greets person based on time of day
def timeGreeting(hour, name):
	engine = pyttsx3.init()
	setUpEngine(engine)
	if 5 <= hour <= 11:
		print(f"Good morning, {name}!")
		engine.say(f"Good morning, my friend, {name}!")
	elif 12 <= hour <= 17:
		print(f"Good afternoon, {name}!")
		engine.say(f"Good afternoon, {name}!")
	else:
		print(f"Good evening, {name}!")
		engine.say(f"Good evening, {name}!")
	engine.runAndWait()

# engine.say(f"I

timeGreeting(time, NAME)

ON = True;
while ON:
	try: 
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.4)

			#listens for the user's input
			audio2 = r.listen(source2)

			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			# for recognizing "open" command followed by app in Apps list

			if MyText == "go to sleep":
				SpeakText(f"Goodbye, {NAME}")
				ON = False
				break

			if MyText == "quote":
				quote = random.choice(ql)
				print(quote)
				SpeakText(quote)

			# opens application with keyphrase "open [app name shorthand(e.g. chrome)]"
			command, appName = MyText[:4], MyText[5:]

			if command == "open" and appName in Apps.keys():
				print("Opening " + Apps[appName]["appName"])
				SpeakText("Opening, "  + Apps[appName]["appName"])
				os.system("open " + Apps[appName]["Path"])
			elif command == "open" and appName not in Apps.keys(): # and appName != "quote" or appName != "quot"
				print(f"Sorry {NAME}, I can't find that app.")
				SpeakText(f"Sorry {NAME}, I can't find that app.")
			else:
				continue

	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))
	     
	except sr.UnknownValueError:
	    print("unknown error occured")


