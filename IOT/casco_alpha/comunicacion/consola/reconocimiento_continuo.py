import speech_recognition as sr
import datetime

r = sr.Recognizer()
trigger_word = "Toni"
exit_commands = ["salir", "apagar jarvis"]

def responder_comando(pregunta):
    if "hora" in pregunta:
        print("La hora es:", datetime.datetime.now().strftime("%H:%M"))
    else:
        print("No entiendo la pregunta.")

with sr.Microphone(device_index=1) as source:
    print("Esperando palabra clave...")
    while True:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language="es-ES").lower()

            if trigger_word in text:
                print("Palabra clave detectada. Jarvis está escuchando... (di 'salir' para terminar)")

                while True:
                    try:
                        print("Esperando pregunta...")
                        audio = r.listen(source)
                        pregunta = r.recognize_google(audio, language="es-ES").lower()
                        print(f"Has dicho: {pregunta}")

                        if any(cmd in pregunta for cmd in exit_commands):
                            print("Saliendo del modo escucha. Hasta luego.")
                            exit()

                        responder_comando(pregunta)
                    except sr.UnknownValueError:
                        print("No se entendió la pregunta. Intenta de nuevo.")
            else:
                print("No se detectó la palabra clave.")
        except sr.UnknownValueError:
            print("No se entendió el audio.")