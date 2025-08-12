import speech_recognition as sr
import datetime

r = sr.Recognizer()
trigger_word = "tony"

# Reemplaza 3 por el índice real de tu micrófono USB
with sr.Microphone(device_index=1) as source:
    print("Esperando palabra clave...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-ES").lower()
        if trigger_word in text:
            print("Palabra clave detectada. Esperando pregunta...")
            audio = r.listen(source)
            pregunta = r.recognize_google(audio, language="es-ES").lower()
            print(f"Has dicho: {pregunta}")
            if "hora" in pregunta:
                print("La hora es:", datetime.datetime.now().strftime("%H:%M"))
            else:
                print("No entiendo la pregunta.")
        else:
            print("No se dijo la palabra clave.")
    except sr.UnknownValueError:
        print("No se entendió el audio.")
