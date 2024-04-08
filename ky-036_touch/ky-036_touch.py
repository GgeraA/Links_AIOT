from machine import Pin
import time

# Configuración del pin del sensor táctil KY-036 (Touch)
touch_pin = Pin(34, Pin.IN)

# Bucle principal
while True:
    # Leer el estado del sensor táctil KY-036 (Touch)
    touch_state = touch_pin.value()
    
    # Verificar si el sensor táctil está tocado
    if touch_state == 0:
        print("No tocado")
    else:
        print("Tocado")
    time.sleep(2)
