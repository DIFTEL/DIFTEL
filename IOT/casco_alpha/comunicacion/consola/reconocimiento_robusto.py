import speech_recognition as sr
import datetime
import time

r = sr.Recognizer()
trigger_word = "tony"
exit_commands = ["salir", "apagar jarvis"]

def responder_comando(pregunta):
    if "hora" in pregunta:
        print("La hora es:", datetime.datetime.now().strftime("%H:%M"))
    else:
        print("No entiendo la pregunta.")

def escuchar_audio(source, timeout=5, phrase_time_limit=5):
    """Función segura para escuchar audio sin bloquear indefinidamente"""
    try:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        texto = r.recognize_google(audio, language="es-ES").lower()
        return texto
    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        print("No se entendió lo que dijiste.")
        return None
    except sr.RequestError as e:
        print(f"Error con el servicio de reconocimiento: {e}")
        return None

with sr.Microphone(device_index=1) as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("✅ Jarvis activo. Di 'tony' para empezar.")

    while True:
        print("🎤 Esperando palabra clave...")
        texto = escuchar_audio(source)

        if texto and trigger_word in texto:
            print("🔓 Activación detectada. Jarvis escuchando... (di 'salir' para apagar)")
            while True:
                print("❓ ¿Cuál es tu pregunta?")
                pregunta = escuchar_audio(source)

                if pregunta:
                    print(f"👉 Has dicho: {pregunta}")
                    if any(cmd in pregunta for cmd in exit_commands):
                        print("🛑 Jarvis se despide. Hasta luego.")
                        exit()
                    responder_comando(pregunta)
                else:
                    print("🔁 Sin entrada válida. Vuelve a intentar.")
        elif texto:
            print("⚠️ No se detectó palabra clave.")