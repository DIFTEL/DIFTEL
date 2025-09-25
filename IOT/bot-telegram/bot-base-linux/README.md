# bot-telegram

## ✅ 1. Crear y preparar el entorno virtual de Python

```bash
# Paso 1: Instalar virtualenv si no lo tienes
sudo apt update
sudo apt install python3-venv -y

# Paso 2: Crear una carpeta para tu proyecto
mkdir ~/telegram_bot
cd ~/telegram_bot

# Paso 3: Crear un entorno virtual
python3 -m venv venv

# Paso 4: Activar el entorno virtual
source venv/bin/activate

# Paso 5: Instalar las dependencias necesarias
pip install telepot

```

## ✅ 2. Crear el script bot_ip_wifi.py

```bash
nano bot.py
```

Hazlo ejecutable
```bash
chmod +x bot.py
```

## ✅ 3. Crear archivo de servicio systemd

Esto hará que el bot se levante automáticamente al inicio.

```bash
sudo nano /etc/systemd/system/telegram_bot.service
```

Contenido del archivo:
```bash
[Unit]
Description=Bot Telegram IP WiFi
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=[nombre de usuario]
WorkingDirectory=/home/[nombre de usuario]/telegram_bot
ExecStart=/home/[nombre de usuario]/telegram_bot/venv/bin/python3 /home/pi/telegram_bot/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## ✅ 4. Habilitar y probar el servicio

```bash
# Recargar systemd
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

# Habilitar para que se inicie automáticamente
sudo systemctl enable telegram_bot_ip.service

# Iniciar el servicio
sudo systemctl start telegram_bot_ip.service

# Verificar su estado
sudo systemctl status telegram_bot_ip.service
```

## ✅ 5. Probar el comando /get_ip desde Telegram

En tu chat de Telegram, envía el comando:

```bash
/get_ip
```
Deberías recibir un mensaje como:

```bash
📡 Conectado a: MiRedWiFi
🌐 IP: 192.168.1.42
```