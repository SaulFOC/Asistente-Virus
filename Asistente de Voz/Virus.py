#descripcion: Programa que reconoce voz y la convierte en texto
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia


name="virus"
#la variable listener es para escuchar en el microfono con la funcion de speech_recognition
#la variable engine es para que hable con la funcion de pyttsx3
listener=sr.Recognizer()

engine=pyttsx3.init()


#importando todas las voces que tiene el programa
voces=engine.getProperty("voices")

engine.setProperty("voice", voces[0].id)

#funcion para que hable el programa
def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
#el try es para que no se caiga el programa si no se escucha nada
    try:
        with sr.Microphone() as source:   
            print("Escuchando...")
            voice=listener.listen(source)
            rec=listener.recognize_google(voice, language="es-US")
            rec=rec.lower()
            if name in rec:
                rec=rec.replace(name, '')
                print(rec)
            else:
                talk("No te entendi, repite por favor")
    except:
        pass
    return rec

def run():
    rec=listen()
    if 'reproduce' in rec:
        song=rec.replace('reproduce', '')
        talk('Reproduciendo'+song)
        pywhatkit.playonyt(song)
    elif 'hora' in rec:
        hora=datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las"+hora+"de la tarde")
    elif 'informacion' in rec:
        busqueda=rec.replace('informacion', '')
        talk('Buscando'+busqueda)
        pywhatkit.search(busqueda)
    elif 'busca' in rec:
        order=rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'envia' in rec:
        talk('¿A quien le quieres enviar el mensaje?')
        contacto=listen()
        talk('¿Que le quieres decir?')
        mensaje=listen()
        pywhatkit.sendwhatmsg(contacto, mensaje, 16, 30)

while True:
    run()

