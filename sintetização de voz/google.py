from gtts import gTTS
import os
#from pygame import mixer

#usando a biblioteca os
som = gTTS("Ola,vamos sintetizar voz com python", lang= 'pt')
som.save('som1.mp3')

os.system('som1.mp3')


#Usando a biblioteca pygame

som = gTTS("Ola,vamos sintetizar voz com python", lang= 'pt')
som.save('som.mp3')

os.system('som.mp3')

#mixer.init()
#mixer.music.load('som.mp3')
#mixer.music.play()

#r = input("digite algo para finalizar  ")


#Biblioteca que salva um arquivo de som
