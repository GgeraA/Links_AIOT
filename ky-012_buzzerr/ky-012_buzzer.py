from machine import Pin
import time

# Configuración del pin para controlar el zumbador (buzzer)
buzzer_pin = Pin(13, Pin.OUT)

# Función para hacer sonar el zumbador
def buzz(duration_ms):
    buzzer_pin.on()  # Encender el zumbador
    time.sleep_ms(duration_ms)  # Esperar la duración especificada
    buzzer_pin.off()  # Apagar el zumbador

# Bucle principal
while True:
    # Hacer sonar el zumbador durante 500 ms
    buzz(800)
    # Esperar 1 segundo entre cada zumbido
    time.sleep(1)
