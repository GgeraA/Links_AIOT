from machine import Pin, PWM
import time

# Configuración de los pines del botón y del zumbador pasivo
buzzer_pin = Pin(13, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

# Función para generar un tono en el zumbador
def buzz(frequency, duration):
    buzzer_pwm.freq(frequency)  # Establece la frecuencia del tono
    buzzer_pwm.duty(512)        # Establece el ciclo de trabajo al 50%
    time.sleep(duration)        # Espera durante la duración especificada
    buzzer_pwm.duty(0)          # Apaga el zumbador

# Bucle principal
while True:
        buzz(1000, 0.5)         # Genera un tono de 1000 Hz durante 0.5 segundos
        time.sleep(0.2)         # Espera un corto tiempo para evitar repeticiones rápidas
