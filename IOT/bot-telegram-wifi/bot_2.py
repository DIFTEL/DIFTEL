#!/usr/bin/env python3
import os
import socket
import subprocess
import telepot
import time
from datetime import timedelta

# === CONFIGURACIÓN ===

# Configura tu token y chat ID
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'


# === FUNCIONES AUXILIARES ===

# Función para obtener IP y nombre de la red
def get_connection_info():
    try:
        # Obtener dirección IP (interfaz con salida a Internet)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "IP no disponible"

    # Obtener nombre de red WiFi si es aplicable
    try:
        ssid = subprocess.check_output(["iwgetid", "-r"], stderr=subprocess.DEVNULL).decode().strip()
        if not ssid:
            ssid = "Ethernet u otra conexión"
    except Exception:
        ssid = "No conectado o interfaz no disponible"

    return ip_address, ssid

# Función para enviar mensaje por Telegram
def enviar_mensaje(chat_id=None):
    ip, ssid = get_connection_info()
    mensaje = f"📡 Conectado a: {ssid}\n🌐 IP: {ip}"
    destino = chat_id if chat_id else TELEGRAM_CHAT_ID
    bot.sendMessage(destino, mensaje)
    print(f"[INFO] Enviado: {mensaje}")


def get_uptime():
    with open('/proc/uptime', 'r') as f:
        segundos = float(f.readline().split()[0])
    return str(timedelta(seconds=int(segundos)))

def get_hostname():
    return socket.gethostname()

def get_status():
    # Temperatura
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    except:
        temp = "Temperatura no disponible"
    
    # RAM y CPU
    try:
        ram = subprocess.check_output(["free", "-h"]).decode()
        cpu = subprocess.check_output(["top", "-bn1"]).decode()
    except:
        ram = cpu = "No disponible"

    # Espacio en disco
    try:
        disk = subprocess.check_output(["df", "-h", "/"]).decode()
    except:
        disk = "No disponible"

    return f"🌡 {temp.strip()}\n\n📊 RAM:\n{ram}\n📈 CPU:\n{cpu.splitlines()[2]}\n💾 Disco:\n{disk}"

def show_help():
    return (
        "Comandos disponibles:\n"
        "/get_ip - IP y red conectada\n"
        "/uptime - Tiempo encendida\n"
        "/hostname - Nombre del dispositivo\n"
        "/reboot - Reinicia la Raspberry\n"
        "/status - Info del sistema\n"
        "/comandos - Ver esta ayuda"
    )

# === MANEJADOR DE MENSAJES ===

def handle(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            return

        cmd = msg['text'].strip()

        if str(chat_id) != TELEGRAM_CHAT_ID:
            bot.sendMessage(chat_id, "⛔ Acceso denegado.")
            return

        if cmd == '/get_ip':
            enviar_mensaje(chat_id)
        elif cmd == '/uptime':
            bot.sendMessage(chat_id, f"⏱ Uptime: {get_uptime()}")
        elif cmd == '/hostname':
            bot.sendMessage(chat_id, f"📛 Hostname: {get_hostname()}")
        elif cmd == '/reboot':
            bot.sendMessage(chat_id, "🔁 Reiniciando Raspberry...")
            time.sleep(2)
            os.system("sudo reboot")
        elif cmd == '/status':
            bot.sendMessage(chat_id, get_status())
        elif cmd == '/comandos':
            bot.sendMessage(chat_id, show_help())
        else:
            bot.sendMessage(chat_id, "❓ Comando no reconocido. Escribe /comandos para ayuda.")
    except Exception as e:
        print(f"[ERROR] {e}")

# === INICIALIZACIÓN ===
bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
bot.message_loop(handle)

print("[INFO] Enviando IP al iniciar...")
enviar_mensaje()

print('[INFO] Bot escuchando comandos...')
while True:
    time.sleep(10)