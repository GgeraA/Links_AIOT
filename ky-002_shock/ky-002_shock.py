from machine import Pin
import time

led_pin = Pin(2, Pin.OUT)  # Pin para controlar el LED
shock_pin = Pin(34, Pin.IN)   # Pin para leer el sensor KY-002

# Bucle principal
while True:
    val = shock_pin.value()  # Leer el valor del sensor KY-002
    
    if val == 1:  # Cuando el sensor detecta un choque, el LED parpadea
        led_pin.off() 
        print("Detección OFF...")
    else:
        led_pin.on()
        print("Detección ON...")
        time.sleep(2)
