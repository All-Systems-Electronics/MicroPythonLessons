from machine import Pin, PWM
import time

# Create a PWM object using GP15.
beeper_pwm = PWM(Pin(15))
# Set the initial duty cycle to 0 to disable the toggling of the pin.
beeper_pwm.duty_u16(0)

def beep(freq: int):
    if freq < 100:
        # Turn the beeper off by setting a default frequency and a duty cycle of 0.
        beeper_pwm.freq(5000)
        beeper_pwm.duty_u16(0)
    else:
        # Set the frequency desired by the caller.
        beeper_pwm.freq(freq)
        # Set the duty cycle to 50%, where 65535 is the maximum possible value.
        beeper_pwm.duty_u16(65535 / 2)

while True:
    beep(800)
    time.sleep_ms(500)
    beep(1000)
    time.sleep_ms(500)
    beep(1200)
    time.sleep_ms(500)
    beep(0)
    time.sleep_ms(1000)
