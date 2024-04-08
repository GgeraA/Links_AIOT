from machine import Pin
import time

# Configuración del pin del sensor Reed Switch
reed_switch_pin = Pin(34, Pin.IN)

# Bucle principal
while True:
    # Leer el estado del sensor Reed Switch (0 para contacto magnético detectado, 1 para no detectado)
    switch_state = reed_switch_pin.value()

    # Verificar si se detecta el contacto magnético
    if switch_state == 1:
        print("Ningún contacto magnético detectado")
    else:
        print("Contacto magnético detectado")

    time.sleep(3)  # Espera 3 segundos antes de la próxima lectura
