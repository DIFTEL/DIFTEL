"""
Script de ejemplo: responde a preguntas específicas reproduciendo audios pregrabados.
Requiere: instalar pygame (pip install pygame) y SpeechRecognition (pip install SpeechRecognition)
Coloca los archivos de audio en la misma carpeta que este script.
"""
import pygame
import time
import sys
import speech_recognition as sr # Added import
import os # Added import for path manipulation

# Get the absolute path of the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Diccionario de preguntas y archivos de audio asociados
# Ensure the filenames here match exactly, including case, with your audio files
RESPUESTAS = {
    "qué es telemática": "respuesta_telematica.wav",
    "quién eres": "respuesta_seria.wav",
    "suena familiar tu voz": "respuesta_iron_man.wav",
    "cerremos la presentación": "cierre_presentacion.wav",
    "es curioso": "curioso.wav"
}

# --- Speech Recognition Setup ---
r = sr.Recognizer()
trigger_word = "casco"  # You can change this trigger word
exit_commands = ["salir", "adiós", "terminar"] # Voice commands to exit

def escuchar_audio(source, timeout=5, phrase_time_limit=5):
    """Función para escuchar audio y reconocerlo."""
    print("🎤 Escuchando...")
    try:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        texto = r.recognize_google(audio, language="es-ES").lower()
        print(f"Has dicho: {texto}")
        return texto
    except sr.WaitTimeoutError:
        print("No se detectó audio en el tiempo esperado.")
        return None
    except sr.UnknownValueError:
        print("No se entendió lo que dijiste.")
        return None
    except sr.RequestError as e:
        print(f"Error con el servicio de reconocimiento de voz; {e}")
        return None
# --- End Speech Recognition Setup ---

def reproducir_audio(archivo_relativo):
    pygame.mixer.init() # Initialize mixer here if not already globally initialized
    # Construct the absolute path to the audio file
    ruta_absoluta_audio = os.path.join(SCRIPT_DIR, archivo_relativo)
    print(f"Intentando cargar audio desde: {ruta_absoluta_audio}") # Debugging line
    try:
        pygame.mixer.music.load(ruta_absoluta_audio)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except pygame.error as e:
        print(f"Error al cargar o reproducir el audio '{ruta_absoluta_audio}': {e}")

if __name__ == "__main__":
    pygame.init() # Initialize all pygame modules, including mixer
    print("Inicializando J.A.R.V.I.S. con reconocimiento de voz...")
    # It's good practice to list microphones if the user has issues
    # print("Micrófonos disponibles:", sr.Microphone.list_microphone_names())
    # You might need to change device_index if you have multiple microphones
    # For device_index, you might need to experiment. If default doesn't work, try 0, 1, 2, etc.
    # Or let the user specify it. For now, using default.
    try:
        with sr.Microphone() as source: # Using default microphone
            print("Ajustando para ruido ambiental, por favor espera...")
            r.adjust_for_ambient_noise(source, duration=1)
            print(f"✅ J.A.R.V.I.S. listo. Di '{trigger_word}' para activarme.")

            while True:
                print(f"🎤 Esperando la palabra clave '{trigger_word}'...")
                texto_activacion = escuchar_audio(source, timeout=10, phrase_time_limit=5)

                if texto_activacion and trigger_word in texto_activacion:
                    print(f"🔓 {trigger_word.capitalize()} activado. ¿Cuál es tu pregunta?")
                    while True:
                        pregunta = escuchar_audio(source, timeout=7, phrase_time_limit=7)

                        if pregunta:
                            if pregunta in RESPUESTAS:
                                print(f"Reproduciendo respuesta para: {pregunta}")
                                reproducir_audio(RESPUESTAS[pregunta])
                                print(f"✅ J.A.R.V.I.S. listo. Di '{trigger_word}' para activarme o una pregunta si ya estoy activo.")
                                break # Break from inner loop, back to waiting for trigger word
                            elif any(cmd in pregunta for cmd in exit_commands):
                                print("Adiós.")
                                reproducir_audio("cerrando_programa.wav") # Play exit sound
                                pygame.quit()
                                sys.exit(0)
                            else:
                                print("No tengo una respuesta grabada para esa pregunta.")
                        else:
                            # If escuchar_audio returned None (timeout, couldn't understand)
                            print("No he entendido la pregunta o no he detectado audio. Intenta de nuevo.")
                        # Stay in "activated" mode until a valid command or exit
                elif texto_activacion and any(cmd in texto_activacion for cmd in exit_commands):
                    print("Adiós.")
                    reproducir_audio("cerrando_programa.wav") # Play exit sound
                    pygame.quit()
                    sys.exit(0)
                # else: # Optional: feedback if something was heard but not the trigger word
                    # print(f"⚠️ No se detectó la palabra clave '{trigger_word}'.")

    except OSError as e:
        print(f"Error al acceder al micrófono: {e}")
        print("Asegúrate de que tienes un micrófono conectado y configurado.")
        print("Puedes necesitar instalar 'portaudio' o similar (sudo apt-get install portaudio19-dev python3-pyaudio on Debian/Ubuntu)")
        print("O en Windows, asegúrate de que el micrófono tiene permisos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        pygame.quit()