from machine import Pin, ADC
import time

# Configuración del pin del sensor Hall
hall_sensor_pin = Pin(34, Pin.IN)
adc = ADC(hall_sensor_pin)

# Función para leer el valor del sensor Hall
def read_hall_sensor():
    return adc.read()

# Bucle principal
while True:
    hall_value = read_hall_sensor()
    print("Valor del sensor Hall:", hall_value)
    time.sleep(3)  # Espera 3 segundos antes de leer nuevamente
