from machine import Pin
import time

# Configuración del pin del sensor KY-027.
sensor_pin = Pin(34, Pin.IN)
led_pin = Pin(13, Pin.OUT)

# Bucle principal
while True:
    # Leer el estado del sensor
    sensor_state = sensor_pin.value()
    
    # Encender el LED si se detecta una inclinación (sensor activado)
    if sensor_state == 1:
        led_pin.on()
        print("Inclinación detectada");
        time.sleep(3)  # Espera 3 segundos antes de leer nuevamente
    else:
        led_pin.off()
        print("No hay inclinación detectada");
        time.sleep(3)  # Espera 3 segundos antes de leer nuevamente
