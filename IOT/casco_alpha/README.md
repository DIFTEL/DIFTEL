# J.A.R.V.I.S. Iron Man Helmet Project

Este proyecto busca crear un casco interactivo inspirado en Iron Man, usando una Raspberry Pi como cerebro principal y un Arduino para el control de servomotores. El objetivo es desarrollar un asistente virtual modular, replicable y mejorable, pensado para demostraciones educativas y ferias tecnológicas.

## Estructura del Proyecto

La organización del repositorio sigue un enfoque modular y por áreas funcionales, facilitando el desarrollo incremental y la colaboración.

```
/comunicacion/
  /consola/
    reconocimiento_basico.py
    reconocimiento_continuo.py
    reconocimiento_robusto.py
    README.md
  /audio/
    respuesta_audio.py
    README.md
/hardware/
  /arduino_servos/
    control_servos.ino
    README.md
/integracion/
  raspberry_arduino.py
  README.md
/docs/
  arquitectura.md
  ideas_futuras.md
README.md
```

### Áreas y Etapas

- **/comunicacion/**  
  Desarrollo del asistente virtual en la Raspberry Pi.  
  - **/consola/**: Versiones iniciales que responden por consola.  
  - **/audio/**: Versiones que responden con audios pregrabados o síntesis de voz.

- **/hardware/**  
  Control de servomotores y otros actuadores con Arduino.

- **/integracion/**  
  Comunicación entre Raspberry Pi y Arduino para controlar el casco.

- **/docs/**  
  Documentación técnica, arquitectura y propuestas de mejora.

---

## Descripción de las Áreas

### 1. Comunicación (Raspberry Pi)

#### a) Consola

Scripts que permiten activar el asistente por palabra clave y responder preguntas por consola.  
Evolución:
- `reconocimiento_basico.py`: Reconocimiento de palabra clave y una pregunta.
- `reconocimiento_continuo.py`: Reconocimiento continuo, múltiples preguntas.
- `reconocimiento_robusto.py`: Manejo robusto de errores, tolerancia a silencios, uso de timeout, etc.

#### b) Audio

Scripts que permiten responder con audios pregrabados o síntesis de voz.  
Evolución:
- `respuesta_audio.py`: Responde a preguntas específicas con audios grabados.
- Futuras versiones: integración de TTS offline (pyttsx3, gTTS, Vosk, Whisper, etc).

### 2. Hardware (Arduino)

Control de servomotores para abrir/cerrar el casco y otros actuadores.  
- `control_servos.ino`: Código Arduino para controlar uno o varios servos.

### 3. Integración

Scripts y documentación para la comunicación entre Raspberry Pi y Arduino, permitiendo que el asistente virtual controle los servos del casco.

---

## Desarrollo Incremental

El proyecto está pensado para evolucionar en etapas claras:

1. **Reconocimiento y respuesta por consola**  
   (Ver `/comunicacion/consola/`)

2. **Respuesta con audios pregrabados o TTS**  
   (Ver `/comunicacion/audio/`)

3. **Control de hardware (servos) con Arduino**  
   (Ver `/hardware/arduino_servos/`)

4. **Integración Raspberry Pi ↔ Arduino**  
   (Ver `/integracion/`)

---

## Ejemplo de Uso

### 1. Comunicación por Consola

```bash
cd comunicacion/consola
python reconocimiento_basico.py
```

### 2. Respuesta con Audio

```bash
cd comunicacion/audio
python respuesta_audio.py
```

### 3. Control de Servos

Sube el código de `/hardware/arduino_servos/control_servos.ino` a tu Arduino.

### 4. Integración

Ejecuta el script de `/integracion/` para conectar la Raspberry Pi con el Arduino.

### Área de Integración

El directorio `integracion` contiene los scripts necesarios para conectar la Raspberry Pi con el Arduino y controlar el casco de Iron Man. Incluye versiones para control por consola, por voz y por voz con respuestas de audio.

#### Estructura

- `consola/raspberry_arduino.py`: Control del casco mediante comandos escritos en consola.
- `audio/raspberry_arduino_voz.py`: Control del casco mediante comandos de voz.
- `audio/raspberry_arduino_voz_audio.py`: Control del casco por voz y reproducción de audios pregrabados como respuestas.

#### Replicación paso a paso

1. Clona el repositorio y navega a la carpeta `integracion`.
2. Crea y activa un entorno virtual llamado `jarvis_integracion_env`:
   ```powershell
   python -m venv jarvis_integracion_env
   .\jarvis_integracion_env\Scripts\Activate.ps1
   ```
3. Actualiza pip:
   ```powershell
   python -m pip install --upgrade pip
   ```
4. Instala las dependencias necesarias:
   ```powershell
   pip install pyserial SpeechRecognition pyaudio pygame
   ```
5. Conecta el Arduino y verifica el puerto (ej: COM3, /dev/ttyACM0).
6. Ejecuta el script deseado:
   - Por consola:
     ```powershell
     cd consola
     python raspberry_arduino.py
     ```
   - Por voz:
     ```powershell
     cd ..\audio
     python raspberry_arduino_voz.py
     ```
   - Por voz y audio:
     ```powershell
     python raspberry_arduino_voz_audio.py
     ```

#### Notas
- Puedes modificar los scripts para adaptar los comandos o el puerto serie según tu sistema.
- El entorno virtual `jarvis_integracion_env` es independiente del resto del proyecto para evitar conflictos de dependencias.
- Para la versión con audio, coloca los archivos de audio en la misma carpeta y edita el diccionario de respuestas según tus necesidades.

---

## Recomendaciones y Futuras Mejoras

- Añadir feedback de voz con pyttsx3 o gTTS.
- Implementar modelos offline (Vosk, Whisper) para reconocimiento sin internet.
- Mejorar la integración hardware-software.
- Documentar la arquitectura y posibles expansiones en `/docs/`.

---

## Créditos y Contacto

Proyecto desarrollado por estudiantes de Ingeniería Civil Telemática, área IoT de DIFTEL.

---

## Licencia