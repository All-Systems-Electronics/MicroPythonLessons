# Import the Pin class from the machine module so we don't need to keep typing machine.Pin
from machine import Pin
# Import the time module so we can use the sleep functions.
import time

# Configure the external LED on GPIO 20 as a digital output, initially turned off.
# The result of this configuration is returned as an object and stored in the led variable.
led = Pin(20, mode=Pin.OUT, value=0)

while True:
    led.value(0)
    print(f"The LED value is {led.value()}")
    time.sleep_ms(1000)
    led.value(1)
    print(f"The LED value is {led.value()}")
    time.sleep_ms(1000)
