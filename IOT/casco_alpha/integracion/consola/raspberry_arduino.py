"""
Script de integración entre Raspberry Pi y Arduino para el control del casco de Iron Man.

Este script permite enviar comandos desde la Raspberry Pi al Arduino a través del puerto serie,
para abrir o cerrar el casco mediante servomotores.

Requisitos:
- Instalar pyserial: pip install pyserial
- Conectar Arduino por USB y conocer el puerto (ej: COM3 en Windows, /dev/ttyACM0 en Linux)
"""
import serial
import time

# Configura el puerto serie según tu sistema
PUERTO = 'COM3'  # Cambia esto por el puerto correcto
BAUDIOS = 9600

try:
    arduino = serial.Serial(PUERTO, BAUDIOS, timeout=2)
    time.sleep(2)  # Espera a que el Arduino reinicie
except Exception as e:
    print(f"No se pudo conectar al Arduino: {e}")
    exit(1)

def enviar_comando(comando):
    arduino.write((comando + '\n').encode())
    respuesta = arduino.readline().decode().strip()
    return respuesta

if __name__ == "__main__":
    print("Control de casco J.A.R.V.I.S. (abrir/cerrar)")
    while True:
        cmd = input("Comando (abrir/cerrar/salir): ").strip().lower()
        if cmd in ["abrir", "cerrar"]:
            resp = enviar_comando(cmd)
            print(f"Arduino: {resp}")
        elif cmd in ["salir", "exit", "quit"]:
            print("Saliendo...")
            break
        else:
            print("Comando no válido. Usa 'abrir', 'cerrar' o 'salir'.")