import pyttsx3
import speech_recognition as sr
import os

en = pyttsx3.init()
en.say('Olasenhor,se voce deseja ouvir a sua musica respondasim,caso contratio,responda não')
en.setProperty('voice',b'brasil')
en.setProperty('rate', 140)
en.setProperty('volume', 1)
en.runAndWait()

recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')