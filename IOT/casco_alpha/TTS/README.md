# Clonación de Voz con Coqui TTS (Modelo XTTS v2)

Este proyecto demuestra cómo utilizar Coqui TTS, específicamente el modelo `xtts_v2`, para la clonación de voz a partir de un archivo de audio de referencia. El notebook principal para esta demostración es `coqui_clone_xtts_v2.ipynb`.

## Requisitos Previos

1.  **Python:** Se recomienda Python 3.11. Versiones más recientes (como Python 3.12+) pueden tener problemas de compatibilidad con algunas dependencias de Coqui TTS.
2.  **Git:** Para clonar repositorios si es necesario (aunque Coqui TTS se instala vía pip).
3.  **FFmpeg (Opcional pero Recomendado):** Para el manejo de diversos formatos de audio. Puedes descargarlo desde [ffmpeg.org](https://ffmpeg.org/download.html) y asegurarte de que esté en el PATH de tu sistema.

## Configuración del Entorno

Es crucial configurar el entorno correctamente para evitar conflictos de dependencias.

1.  **Crear un Entorno Virtual:**
    ```bash
    python -m venv .venv-py311
    ```
    (Reemplaza `.venv-py311` con el nombre que prefieras para tu entorno).

2.  **Activar el Entorno Virtual:**
    *   En Windows (PowerShell/CMD):
        ```bash
        .\.venv-py311\Scripts\activate
        ```
    *   En macOS/Linux:
        ```bash
        source .venv-py311/bin/activate
        ```

3.  **Instalar Dependencias:**
    Instala las versiones específicas de las bibliotecas que han demostrado ser compatibles:
    ```bash
    pip install TTS==0.22.0
    pip install transformers==4.33.0
    pip install numpy==1.26.4
    ```
    *Nota: `torch` y `torchaudio` se instalarán como dependencias de `TTS`. Asegúrate de que la versión de `torch` instalada sea compatible con tu hardware (CPU o GPU con CUDA). Si tienes problemas con CUDA, puedes forzar una instalación específica de PyTorch desde su [sitio web oficial](https://pytorch.org/get-started/locally/).*

## Ejecución del Notebook (`coqui_clone_xtts_v2.ipynb`)

1.  **Abrir Jupyter Notebook/Lab:**
    Asegúrate de tener Jupyter instalado (`pip install notebook` o `pip install jupyterlab`). Luego, inicia el servidor:
    ```bash
    jupyter notebook
    # o
    jupyter lab
    ```

2.  **Seleccionar el Kernel Correcto:**
    Dentro de Jupyter, asegúrate de que el kernel seleccionado para el notebook `coqui_clone_xtts_v2.ipynb` sea el entorno virtual que creaste (ej. `.venv-py311`).

3.  **Pasos Clave en el Notebook:**

    *   **Añadir Clases a Globales Seguros de PyTorch:**
        Debido a cambios en `torch.load` a partir de PyTorch 2.6, es necesario añadir explícitamente ciertas clases a los "globales seguros" antes de cargar modelos XTTS. El notebook contiene una celda para esto, que incluye:
        ```python
        import torch
        import importlib

        classes_to_make_safe = [
            "TTS.tts.configs.xtts_config.XttsConfig",
            "TTS.tts.models.xtts.XttsAudioConfig",
            "TTS.config.shared_configs.BaseDatasetConfig",
            "TTS.tts.models.xtts.XttsArgs"
        ]

        # ... (código para importar y añadir las clases) ...
        # torch.serialization.add_safe_globals([actual_class])
        ```
        Ejecuta esta celda primero.

    *   **Cargar el Modelo XTTS v2:**
        El modelo se carga especificando su nombre y moviéndolo al dispositivo adecuado (CPU o GPU).
        ```python
        from TTS.api import TTS
        import torch

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_name_v2 = "tts_models/multilingual/multi-dataset/xtts_v2"
        
        tts_v2 = TTS(model_name=model_name_v2).to(device)
        ```

    *   **Preparar el Audio de Referencia:**
        Coloca tu archivo de audio de referencia (ej. `iron_voice.WAV`) en una carpeta accesible, por ejemplo, `audio_in/`.

    *   **Síntesis de Voz:**
        Utiliza el método `tts_to_file` para generar el audio.
        ```python
        texto = "Este es el texto que quiero convertir a voz."
        tts_v2.tts_to_file(
            text=texto,
            speaker_wav="audio_in/iron_voice.WAV", # Ruta a tu archivo de voz de referencia
            language="es",                         # Idioma del texto
            file_path="audio_out/nombre_del_archivo.wav" # Ruta donde se guardará el audio generado
        )
        ```
        Asegúrate de que la carpeta de salida (ej. `audio_out/`) exista o créala.

4.  **Reiniciar el Kernel:**
    Si realizas cambios en las bibliotecas instaladas (usando `pip install` en celdas del notebook), **siempre reinicia el kernel de Jupyter** para que los cambios surtan efecto. (En Jupyter: Kernel > Restart Kernel).

## Solución de Problemas Comunes

*   **`UnpicklingError: Unsupported global: GLOBAL ...`**:
    Este error indica que una clase necesaria para deserializar el modelo no está en los globales seguros de PyTorch. Revisa el mensaje de error para identificar la clase (ej. `TTS.alguna.clase.Especifica`) y añádela a la lista `classes_to_make_safe` en la celda correspondiente del notebook. Reinicia el kernel y vuelve a ejecutar.

*   **Conflictos de Dependencias con `numpy` u otras bibliotecas:**
    Si `pip` reporta conflictos, es posible que necesites forzar la reinstalación de una versión específica de la biblioteca en conflicto, como se hizo con `numpy==1.26.4`. Presta atención a los mensajes de error de `pip`.

*   **Errores de CUDA/GPU:**
    Si tienes problemas con la GPU, asegúrate de que tu versión de PyTorch (`torch` y `torchaudio`) sea compatible con tu versión de CUDA y los drivers de tu tarjeta gráfica. Como alternativa, puedes forzar el uso de CPU cambiando `device = "cuda" if torch.cuda.is_available() else "cpu"` a `device = "cpu"`.

Siguiendo estos pasos, deberías poder replicar la funcionalidad del notebook `coqui_clone_xtts_v2.ipynb` y generar voz clonada.
