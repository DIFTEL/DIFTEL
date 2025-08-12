"""
Script: Controla el casco de Iron Man por voz usando Raspberry Pi y Arduino.
- Si se detecta "abrir", envía el comando por serial al Arduino para abrir el casco.
- Si se detecta "cerrar", envía el comando por serial al Arduino para cerrar el casco.
- Si se detecta otra frase, puede reproducir audios como en respuesta_audio.py.
Requiere: pip install pygame SpeechRecognition pyserial
"""
import pygame
import time
import sys
import speech_recognition as sr
import os
import serial

# Configuración del puerto serie (ajusta el nombre del puerto según tu sistema)
SERIAL_PORT = '/dev/ttyACM0'  # Ejemplo para Linux/Raspberry Pi. En Windows sería 'COM3', etc.
BAUD_RATE = 9600

# Get the absolute path of the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

RESPUESTAS = {
    "qué es telemática": "respuesta_telematica.wav",
    "quién eres": "respuesta_seria.wav",
    "suena familiar tu voz": "respuesta_iron_man.wav",
    "cerremos la presentación": "cierre_presentacion.wav",
    "es curioso": "curioso.wav"
}

r = sr.Recognizer()
trigger_word = "casco"
exit_commands = ["salir", "adiós", "terminar"]

# Inicializa el puerto serie
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    time.sleep(2)  # Espera a que el Arduino reinicie
    print(f"✅ Conectado a Arduino en {SERIAL_PORT}")
except Exception as e:
    print(f"⚠️ No se pudo abrir el puerto serie: {e}")
    arduino = None

def escuchar_audio(source, timeout=5, phrase_time_limit=5):
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

def reproducir_audio(archivo_relativo):
    pygame.mixer.init()
    ruta_absoluta_audio = os.path.join(SCRIPT_DIR, archivo_relativo)
    try:
        pygame.mixer.music.load(ruta_absoluta_audio)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except pygame.error as e:
        print(f"Error al cargar o reproducir el audio '{ruta_absoluta_audio}': {e}")

def enviar_comando_arduino(comando):
    if arduino:
        try:
            arduino.write((comando + '\n').encode('utf-8'))
            print(f"Enviado a Arduino: {comando}")
        except Exception as e:
            print(f"Error enviando comando al Arduino: {e}")
    else:
        print("Arduino no conectado. No se puede enviar comando.")

if __name__ == "__main__":
    pygame.init()
    print("Inicializando control de casco por voz...")
    try:
        with sr.Microphone() as source:
            print("Ajustando para ruido ambiental, por favor espera...")
            r.adjust_for_ambient_noise(source, duration=1)
            print(f"✅ Listo. Di '{trigger_word}' para activarme.")

            while True:
                print(f"🎤 Esperando la palabra clave '{trigger_word}'...")
                texto_activacion = escuchar_audio(source, timeout=10, phrase_time_limit=5)

                if texto_activacion and trigger_word in texto_activacion:
                    print(f"🔓 {trigger_word.capitalize()} activado. ¿Qué deseas hacer?")
                    while True:
                        comando = escuchar_audio(source, timeout=7, phrase_time_limit=7)
                        if comando:
                            if "abrir" in comando:
                                enviar_comando_arduino("abrir")
                                print("Comando 'abrir' enviado al casco.")
                                break
                            elif "cerrar" in comando:
                                enviar_comando_arduino("cerrar")
                                print("Comando 'cerrar' enviado al casco.")
                                break
                            elif comando in RESPUESTAS:
                                reproducir_audio(RESPUESTAS[comando])
                                break
                            elif any(cmd in comando for cmd in exit_commands):
                                print("Adiós.")
                                reproducir_audio("cerrando_programa.wav")
                                pygame.quit()
                                if arduino:
                                    arduino.close()
                                sys.exit(0)
                            else:
                                print("No tengo una acción o respuesta para esa frase.")
                        else:
                            print("No he entendido la orden. Intenta de nuevo.")
                elif texto_activacion and any(cmd in texto_activacion for cmd in exit_commands):
                    print("Adiós.")
                    reproducir_audio("cerrando_programa.wav")
                    pygame.quit()
                    if arduino:
                        arduino.close()
                    sys.exit(0)
    except OSError as e:
        print(f"Error al acceder al micrófono: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        pygame.quit()
        if arduino:
            arduino.close()
