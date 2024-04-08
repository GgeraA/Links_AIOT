from machine import Pin
import time

led_pin = Pin(13, Pin.OUT)  # Pin para controlar el KY-034

# Bucle principal
while True:
    led_pin.on()   # Encender LED
    time.sleep(1)  # Esperar 3 segundos
    led_pin.off()  # Apagar LED
    time.sleep(1)  # Esperar 3 segundo
