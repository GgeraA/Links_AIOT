from machine import Pin

# Definición de los pines
ball_switch_pin = Pin(2, Pin.IN)  # Pin del sensor de inclinación (ball switch)

# Bucle principal
while True:
    # Obtener el estado del sensor de inclinación
    tilt_state = ball_switch_pin.value()

    # Comprobar si el sensor de inclinación está inclinado
    if tilt_state == 1:
        led_pin.on()   # Encender el LED
    else:
        led_pin.off()  # Apagar el LED
