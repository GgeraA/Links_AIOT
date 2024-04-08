from machine import Pin
import time

# Configuración del pin del láser
laser_pin = Pin(13, Pin.OUT)

# Función para encender el láser
def turn_on_laser():
    laser_pin.on()

# Bucle principal
while True:
    turn_on_laser()  # Encender el láser