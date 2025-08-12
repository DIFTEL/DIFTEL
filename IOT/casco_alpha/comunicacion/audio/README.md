## Sección de registro de avances para esta sección

# Guía para ejecutar respuesta_audio.py en un entorno virtual Python

Este módulo permite que el asistente J.A.R.V.I.S. responda a preguntas específicas mediante la reproducción de audios pregrabados.

## Requisitos
- Python 3.8 o superior
- Audios en formato .mp3 (colócalos en esta misma carpeta)

## Instalación y uso en entorno virtual

1. **Crea y activa un entorno virtual llamado `jarvis_audio_env`:**

   En PowerShell (Windows):
   ```powershell
   python -m venv jarvis_audio_env
   .\jarvis_audio_env\Scripts\Activate.ps1
   ```

   En Bash (Linux):
   ```bash
   source jarvis_audio_env/bin/activate
   ```

2. **Actualiza pip:**
   ```powershell
   python -m pip install --upgrade pip
   ```

3. **Instala las dependencias necesarias:**
   ```powershell
   pip install pygame
   pip install SpeechRecognition pygame
   ```

4. **Coloca los archivos de audio**
   - Ejemplo: `respuesta_telematica.mp3`, `respuesta_jarvis.mp3`

5. **Ejecuta el script:**
   ```powershell
   python respuesta_audio.py
   ```

## Notas
- Si usas otro sistema operativo, adapta los comandos de activación del entorno virtual.
- Puedes modificar el diccionario de preguntas y respuestas en el script para añadir más audios.

---

**Autor:** Área IoT DIFTEL