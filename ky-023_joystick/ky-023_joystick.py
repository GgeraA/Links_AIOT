from machine import Pin, ADC
import time

# Configuración de los pines para el joystick
x_pin = Pin(34)  # Pin VRx
y_pin = Pin(35)  # Pin VRy
button_pin = Pin(32, Pin.IN, Pin.PULL_UP)  # Pin SW
adc_x = ADC(x_pin)
adc_y = ADC(y_pin)

# Rangos de valores para determinar la dirección del movimiento
THRESHOLD = 1000
CENTER = 2048

# Bucle principal
while True:
    # Leer los valores analógicos de X e Y
    x_value = adc_x.read()
    y_value = adc_y.read()

    # Determinar la dirección del movimiento
    if x_value < CENTER - THRESHOLD:
        print("Joystick movido a la izquierda")
    elif x_value > CENTER + THRESHOLD:
        print("Joystick en posición central")
    elif y_value < CENTER - THRESHOLD:
        print("Joystick movido hacia arriba")
    elif y_value > CENTER + THRESHOLD:
        print("Joystick movido hacia abajo")
    else:
        print("xd")

    # Verificar si se ha presionado el botón
    if button_pin.value() == 0:
        print("Botón del joystick presionado")

    time.sleep(1)  # Espera antes de leer nuevamente para evitar lecturas excesivas
