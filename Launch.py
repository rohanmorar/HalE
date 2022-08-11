import pyttsx3
import os
import time
import speech_recognition as sr

# global vars for name, current hour, voiceID, and voice Rate
NAME = "Rohan"
time = int(time.strftime('%H'))
voiceID = 28 # Other voice ID's -> SHm: 11, SAf: 17, Brf: 28 , YTm : 7, USf: 33, JPf: 18, Spf: 26
RATE = 250

#Applications
Apps = {
    "lol": {"appName": "League of Legends", "Path": "/Applications/League\ of\ Legends.app/"},
    "chrome": {"appName": "Google Chrome", "Path": "/Applications/Google\ Chrome.app/"},
    "fire": {"appName": "Fire Fox", "Path": "/Applications/Firefox.app/"}
    }

myKeys = Apps.keys()

#initializing libraries
# engine = pyttsx3.init()
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
			
			appName = MyText

			if MyText == "go to sleep":
				SpeakText(f"Goodbye, {NAME}")
				ON = False
				break

			for key in Apps:
				if appName not in Apps.keys():
					print(f"Sorry {NAME}, I can't find that app.")
					SpeakText(f"Sorry {NAME}, I can't find that app.")
					break
				elif key == appName:
					print("Opening " + Apps[key]["appName"])
					SpeakText("Opening, "  + Apps[key]["appName"])
					os.system("open " + Apps[key]["Path"])
					break		
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))
	     
	except sr.UnknownValueError:
	    print("unknown error occured")


