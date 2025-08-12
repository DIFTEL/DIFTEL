## Sección de registro de avances para esta sección

# Estructura y funcionamiento del directorio integracion

El directorio `integracion` contiene los scripts y recursos necesarios para conectar la Raspberry Pi con el Arduino, permitiendo que los comandos del asistente virtual se traduzcan en acciones físicas sobre el casco (abrir/cerrar).

## Subdirectorios y archivos

- `consola/raspberry_arduino.py`: Control del casco mediante comandos escritos en consola.
- `audio/raspberry_arduino_voz.py`: Control del casco mediante comandos de voz.

## Requisitos generales
- Raspberry Pi (o PC con Python 3.8+)
- Arduino con el código de control de servos cargado
- Cable USB para conectar Arduino
- Micrófono (para la versión por voz)

## Replicación paso a paso

1. **Clona el repositorio y navega a la carpeta `integracion`**

2. **Crea y activa un entorno virtual llamado `jarvis_integracion_env`:**
   ```powershell
   python -m venv jarvis_integracion_env
   .\jarvis_integracion_env\Scripts\Activate.ps1
   ```

3. **Actualiza pip:**
   ```powershell
   python -m pip install --upgrade pip
   ```

4. **Instala las dependencias necesarias:**
   ```powershell
   pip install pyserial SpeechRecognition pyaudio
   ```
   > Si tienes problemas con pyaudio en Windows, consulta la documentación oficial para instalar la versión adecuada.

5. **Conecta el Arduino y verifica el puerto (ej: COM3, /dev/ttyACM0)**

6. **Ejecuta el script deseado:**
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

## Notas
- Puedes modificar los scripts para adaptar los comandos o el puerto serie según tu sistema.
- El entorno virtual `jarvis_integracion_env` es independiente del resto del proyecto para evitar conflictos de dependencias.

---

**Autor:** Área IoT DIFTEL