import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    print('Diga algo...')
    audio = recon.listen(source)

def method_name():
    return print(recon.recognize_google(audio, language='pt'))

def method_name():
    return method_name()

method_name()
