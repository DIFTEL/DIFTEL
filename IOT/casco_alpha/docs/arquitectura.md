# Arquitectura general del sistema J.A.R.V.I.S.

## Descripción General

El sistema J.A.R.V.I.S. está compuesto por tres módulos principales:

1. **Comunicación (Raspberry Pi):**
   - Procesa el reconocimiento de voz y gestiona la interacción con el usuario.
   - Puede responder por consola, con audios pregrabados o mediante síntesis de voz.

2. **Hardware (Arduino):**
   - Controla los servomotores encargados de abrir y cerrar el casco.
   - Recibe comandos desde la Raspberry Pi a través de comunicación serial.

3. **Integración:**
   - Gestiona la comunicación entre la Raspberry Pi y el Arduino.
   - Permite que las órdenes del asistente virtual se traduzcan en acciones físicas.

## Diagrama de Arquitectura

```
[Usuario]
   |
[Raspberry Pi]
   |-- Comunicación (voz/texto)
   |-- Procesamiento de órdenes
   |
[Serial]
   |
[Arduino]
   |-- Control de servos
   |
[Casco físico]
```

## Flujo de Información

1. El usuario activa el asistente mediante una palabra clave.
2. El sistema reconoce la orden o pregunta.
3. Si es una pregunta, responde por consola o audio.
4. Si es una orden física (abrir/cerrar casco), la Raspberry Pi envía el comando al Arduino.
5. El Arduino ejecuta la acción en el servomotor.

## Modularidad

Cada módulo puede evolucionar de forma independiente, permitiendo mejoras incrementales y facilitando la colaboración.