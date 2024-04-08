from machine import Pin
import time

# Configuración del pin del sensor KY-021 (Mini Switch)
switch_pin = Pin(14, Pin.IN)

# Leer el estado del sensor KY-021 (Mini Switch)
switch_state = switch_pin.value()

# Bucle principal
while True:
    # Verificar si el sensor está activado (campo magnético presente)
    if switch_state == 0:
        print("Campo magnético no detectado")
    else:
        print("Campo magnético detectado")
        
    time.sleep(2)
