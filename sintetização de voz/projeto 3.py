import speech_recognition as sr
import os

print('OLÁ DESEJA ESTAR ACESSANDO A AGENDA?')

recon = sr.Recognizer()

with sr.Microphone() as source:
    audio = recon.listen(source)
resposta = recon.recognize_google(audio, language='pt')

if resposta == "sim":
    print('ABRINDO AGENDA...')
    os.system(r'C:\Users\Felipe Carneiro\OneDrive\Documentos\teste')
elif resposta == "não":
    print("solicitação negada")