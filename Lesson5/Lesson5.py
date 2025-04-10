from machine import Pin
import time

# We enable the internal pull-up resistor for the button so that when the button isn't pressed, the input goes to a known state.
# Otherwise it will probably float, and we won't be able to detect the button press properly.
button = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)

# We need to keep track of the last state of the button by saving it in a variable.
button_last_pressed = not button.value()
led = Pin(20, mode=Pin.OUT, value=0)

while True:
    button_pressed = not button.value()
    
    if button_pressed != button_last_pressed:
        if button_pressed:
            led.toggle()
            print(f"Button was just pressed")
        else:
            print(f"Button was just released")

    button_last_pressed = button_pressed
