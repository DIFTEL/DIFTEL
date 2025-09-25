# Bot Telegram IP WiFi en Windows

Mini guía para implementar un bot de Telegram que obtiene la IP local del equipo en Windows.

## Pasos para la implementación

### 1. Crear carpeta del proyecto

En tu escritorio o donde quieras, crea una carpeta:
```
bot_telegram
```

Dentro estará tu entorno virtual (venv) y tu script `bot_ip_wifi.py`.

### 2. Crear entorno virtual (venv)

Abre PowerShell y navega a la carpeta:
```powershell
cd "C:\Users\Constanza Acosta\Desktop\proyecto_ads_git\bot_telegram"
```

Crea el venv:
```powershell
python -m venv venv
```

Verifica que exista la carpeta `venv\Scripts\python.exe`:
```powershell
dir venv\Scripts\python.exe
```

### 3. Instalar librerías necesarias

Activa el venv usando el .bat (más seguro en Windows):
```powershell
venv\Scripts\activate.bat
```

Instala telepot (y cualquier otra librería que necesites):
```powershell
pip install telepot
```

Verifica las librerías instaladas:
```powershell
pip list
```

### 4. Crear el archivo del bot

En la carpeta `bot_telegram`, crea un archivo llamado: `bot_ip_wifi.py`

El código está disponible en el archivo `bot_ip_wifi.py` (reemplaza `TU_TOKEN_AQUI` por el token de tu bot de Telegram).

### 5. Probar el bot manualmente

Asegúrate de estar en la carpeta del proyecto.

Ejecuta el bot usando Python del venv:
```powershell
venv\Scripts\python.exe bot_ip_wifi.py
```

Deberías ver:
```
Bot activo. Esperando comandos...
```

En Telegram, envía: `/get_ip`

Debes recibir la IP de tu computadora.

### 6. Crear un .bat para ejecutar el bot fácilmente

En la misma carpeta, crea un archivo llamado `iniciar_bot.bat`.

Contenido:
```bat
@echo off
call venv\Scripts\activate.bat
python bot_ip_wifi.py
pause
```

Doble clic en `iniciar_bot.bat` → el bot se inicia sin abrir PowerShell manualmente.

### 7. Ejecutar el bot automáticamente al iniciar Windows

#### 7.1. Programador de Tareas
- Abre Programador de Tareas → Crear tarea básica
- Nombre: `Telegram Bot IP WiFi`
- Desencadenador: Al iniciar sesión o Al iniciar el equipo
- Acción: Iniciar un programa
- Programa/script: ruta al .bat que creaste:
  ```
  C:\Users\Constanza Acosta\Desktop\proyecto_ads_git\bot_telegram\iniciar_bot.bat
  ```
- Carpeta de inicio:
  ```
  C:\Users\Constanza Acosta\Desktop\proyecto_ads_git\bot_telegram
  ```
- Guardar ✅

Ahora tu bot se iniciará automáticamente cada vez que inicies Windows.

## Notas importantes

- No necesitas systemd en Windows. El .bat + Programador de Tareas reemplaza esa funcionalidad.
- Siempre ejecuta tu bot usando Python dentro del venv para evitar problemas de librerías.
- Puedes mantener la ventana abierta para ver los logs, o incluso redirigir la salida a un archivo .log si quieres.

## Instalación de la librería telepot

```powershell
venv\Scripts\activate.bat
pip install telepot
```

## Funcionalidad

El bot implementa:
- Comando `/get_ip`: Obtiene la IP local del equipo
- Respuesta por defecto para otros comandos

## Consideraciones futuras

- Usar un archivo JSON para modificar el token de Telegram e importar el JSON en Python