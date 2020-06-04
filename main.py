import speech_recognition as sr 
import webbrowser
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS 

r = sr.Recognizer()

def record_audio(ask = False):
	with sr.Microphone() as source:
		if ask:
			dexter_speak(ask)
		audio = r.listen(source)
		try:
			voice_data = r.recognize_google(audio)
		except sr.UnkownValueError:
			dexter_speak('sorry, I didnot get that')
		except sr.RequestError:
			dexter_speak('Sorry, my speech service is down')
		return voice_data

def respond(voice_data):
	if 'what is your name' in voice_data:
		dexter_speak("hey! My name is dexter")

	if 'what time is it' in voice_data:
		dexter_speak(ctime())

	if 'search' in voice_data:
		search = record_audio('What do you want me to search')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		dexter_speak('here is what I found about ' + search)

	if 'exit' in voice_data:
		dexter_speak("exiting programe. Take care")
		exit()

def dexter_speak(audio_string):
	tts = gTTS(text = audio_string, lang = 'en')
	r = random.randint(1,1000000)
	audio_file = 'audio' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)


time.sleep(1)
dexter_speak("Hi! How can I help you??")
while 1:
		voice_data = record_audio()
		print(voice_data)
		respond(voice_data)



