from machine import Pin
import time

# Configuración del pin del sensor KY-010 (Light Blocking)
obstacle_pin = Pin(34, Pin.IN)

# Bucle principal
while True:
    # Leer el estado del sensor KY-010 (Light Blocking)
    obstacle_state = obstacle_pin.value()
    
    # Verificar si se detecta un obstáculo (objeto opaco)
    if obstacle_state == 1:
        print("Obstáculo detectado")
        time.sleep(3)
    else:
        print("Ningún obstáculo")
        time.sleep(3)
