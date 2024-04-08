from machine import Pin, ADC
import time

# Configuración del pin analógico A0 como entrada ADC
adc = ADC(Pin(34))
adc.width(ADC.WIDTH_10BIT)  # Establece la resolución de 10 bits (0-1023)
adc.atten(ADC.ATTN_11DB)    # Establece la atenuación a 11 dB

# Función para leer el valor del sensor de sonido
def read_sound_sensor():
    return adc.read()

# Bucle principal
while True:
    sound_value = read_sound_sensor()
    print("Valor del sensor de sonido:", sound_value)
    time.sleep(5.0)  # Espera 5 segundos antes de leer nuevamente
