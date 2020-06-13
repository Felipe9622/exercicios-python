import pyttsx3

en = pyttsx3.init()

nova_velocidade = 50

while nova_velocidade <=150:
    en.setProperty('rate',nova_velocidade)
    en.say("testando velocidade")
    en.runAndWait()
    nova_velocidade = nova_velocidade + 50