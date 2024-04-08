from machine import Pin
import time

# Configuración del pin del sensor de sonido KY-038 (Big Sound)
sound_pin = Pin(34, Pin.IN)

# Bucle principal
while True:
    # Leer el estado del sensor de sonido KY-038 (Big Sound)
    sound_state = sound_pin.value()
    
    # Verificar si se detecta un sonido fuerte
    if sound_state == 1:
        print("Sonido detectado")
    else:
        print("Ningún sonido")
    
    time.sleep(2)  # Esperar un breve período antes de la siguiente lectura
