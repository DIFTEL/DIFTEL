import telepot
import socket

TOKEN = "TU_TOKEN_AQUI"

def get_ip():
    try:
        hostname = socket.gethostname()
        ip_local = socket.gethostbyname(hostname)
        return f"🌐 IP local del equipo: {ip_local}"
    except Exception as e:
        return f"Error al obtener IP: {e}"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == '/get_ip':
            bot.sendMessage(chat_id, get_ip())
        else:
            bot.sendMessage(chat_id, "Usa el comando /get_ip para obtener la IP del equipo.")

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print("Bot activo. Esperando comandos...")

import time
while True:
    time.sleep(10)