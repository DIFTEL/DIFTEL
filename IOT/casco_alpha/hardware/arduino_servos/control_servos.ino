#include <Servo.h>

Servo cascoServo1;
Servo cascoServo2;
const int pinServo1 = 9;  // Pin digital conectado al primer servo
const int pinServo2 = 10; // Pin digital conectado al segundo servo

// Ángulos ajustables para apertura y cierre
const int anguloAbierto = 20;  // Ajusta este valor para el ángulo de apertura
const int anguloCerrado = 200; // Ajusta este valor para el ángulo de cierre

void moverServosSincronizados(int angulo) {
  // Servo 1 se mueve a 'angulo', Servo 2 a '180-angulo' (efecto espejo)
  cascoServo1.write(angulo);
  cascoServo2.write(180 - angulo);
}

void setup() {
  cascoServo1.attach(pinServo1);
  cascoServo2.attach(pinServo2);
  Serial.begin(9600);
  Serial.println("Listo para recibir comandos: 'abrir' o 'cerrar'.");
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();
    if (comando == "abrir") {
      moverServosSincronizados(anguloAbierto);
      Serial.println("Casco abierto");
    } else if (comando == "cerrar") {
      moverServosSincronizados(anguloCerrado);
      Serial.println("Casco cerrado");
    } else {
      Serial.println("Comando no reconocido. Usa 'abrir' o 'cerrar'.");
    }
  }
}