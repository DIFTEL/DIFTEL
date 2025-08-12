# J.A.R.V.I.S

Proyecto de asistente virtual dentro de una Raspeberry Pi con headset  (con entradas separadas de audífonos + micrófono) conectado a través de adaptador USB to jack 3.5. Desarrollo incremental

Pasos para realizar el proyecto en tu máquina desde cero

## 1. 📦 Instalar dependencias necesarias

```bash
sudo apt update
sudo apt install python3-full python3-venv portaudio19-dev python3-pyaudio
sudo apt-get install flac
```

Esto instala:

* Paquetes de desarrollo necesarios (portaudio19-dev, pyaudio)
* Módulo venv para crear entornos virtuales
* El módulo speech_recognition utiliza Google Speech Recognition API, que espera archivos de audio en formato FLAC. Este módulo intenta usar la herramienta flac instalada en tu sistema para hacer la conversión desde el formato WAV que produce PyAudio u otras fuentes.

## 2. 🧪 Crear entorno virtual

```bash
mkdir ~/jarvis_proyecto
cd ~/jarvis_proyecto
python3 -m venv venv
```

## 3. ✅ Activar el entorno virtual

```bash
source venv/bin/activate
```

Cuando esté activado, deberías ver algo así en la terminal:
```bash
(venv) pi@raspberrypi:~/jarvis_proyecto $
```

### 🧼 Salir del entorno virtual
Cuando termines de trabajar:

```bash
deactivate
```

## 4. 📥 Instalar SpeechRecognition y otras librerías dentro del entorno

Con el entorno activado:

```bash
pip install SpeechRecognition
pip install PyAudio
```

⚠️ Si PyAudio da error, puedes instalarlo con apt en lugar de pip:

```bash
Editar
sudo apt install python3-pyaudio
```

## 5. Buscar el indice de tu dispositivo de audio

Utilizando la librería `speech_recognition`, puede encontrar la salida de audio deseada con el siguiente script:

```python
import speech_recognition as sr

r = sr.Recognizer()

# Listar micrófonos
for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {mic_name}")
```

o también,

```python
import speech_recognition as sr

for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {name}")
```

En mi caso obtuve la siguiente salida al final de una larga lista de advertencias típicas cuando ALSA intenta acceder a configuraciones de audio que no existen o no están definidas en el sistem (como surround51, hdmi, iec958, etc).

```bash
0: bcm2835 Headphones: - (hw:0,0)
1: USB PnP Sound Device: Audio (hw:3,0)
2: sysdefault
3: lavrate
4: samplerate
5: speexrate
6: pulse
7: speex
8: upmix
9: vdownmix
10: dmix
11: default
```

Por lo que el indice del dispositivo de salida es 1, información que utilizaremos para los scripts python.

## 6. 🧪 Probar script primera version

Funciona por activación por palabra clave y responde a una sola pregunta.

Ejecuta con

```bash
python reconocimiento_basico.py
```

## 7. 🧪 Probar script segunda version

Modo continuo: Jarvis siempre escuchando y respondiendo múltiples preguntas

* Jarvis se activa al decir "tony".
* Luego entra en modo escucha continua: responde preguntas una tras otra sin tener que reiniciar el script.
* Puedes salir con una palabra como "salir" o "apagar jarvis"

```bash
python reconocimiento_continuo.py
```

## 8. 🧪 Probar script tercera version

Afinar el reconocimiento continuo implica lograr que Jarvis:

✅ Responda fluida y continuamente mientras espera preguntas.

✅ No necesite reiniciarse manualmente para cada pregunta.

✅ Evite errores comunes como quedarse “colgado” o interpretar ruidos como comandos.

✅ Sea tolerante al silencio y maneje errores de escucha.

🔧 Mejoras recomendadas al reconocimiento continuo
Aquí tienes una versión refinada del código con:

* Tiempo máximo de espera (timeout) y duración máxima de escucha (phrase_time_limit).
* Manejo más robusto de errores.
* Detección más clara de “esperando”, “preguntando”, “saliendo”.

✅ Características técnicas incluidas:
adjust_for_ambient_noise: mejora el reconocimiento en ambientes ruidosos.

* timeout: evita que se bloquee esperando audio indefinidamente.
* phrase_time_limit: limita duración de lo que se dice.
* try-except bien distribuido: mayor robustez.

```bash
python reconocimiento_robusto.py
```

## 🔜 Posibles próximos pasos:
* Añadir feedback de voz con pyttsx3.
* Usar un bucle infinito que detecte otras órdenes: abrir apps, consultar clima, reproducir música, etc.
* Entrenar modelos offline con vosk o whisper para no depender de internet.
* Síntesis de voz (text-to-speech) con pyttsx3 o gTTS.
* Reconocimiento de múltiples palabras clave (“tony”, “jarvis”, etc).
* Integración con hardware (LEDs, sensores en Raspberry Pi, etc.).