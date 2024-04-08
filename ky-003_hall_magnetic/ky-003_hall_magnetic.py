from machine import Pin
import time

# Configuración del pin del sensor Hall KY-003
hall_pin = Pin(34, Pin.IN)

# Bucle principal
while True:
    # Leer el estado del sensor Hall KY-003
    hall_state = hall_pin.value()
    
    # Verificar si se detecta un campo magnético
    if hall_state == 0:
        print("Campo magnético detectado")
    else:
        print("Ningún campo magnético")
        
    time.sleep(3)
