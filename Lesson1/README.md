# Lesson 1
This lesson will go through how to connect to the MicroPython shell running on the Pico board.

It will then show how to enter commands into the shell to toggle the onboard LED.

1. Connect the Pico board to the PC using a USB cable.
0. Run __Thonny__, which should have been installed during the [Initial Setup](../README.md).
0. Click on the text in the bottom-right of the Thonny Window.
0. Select __MicroPython (Raspberry Pi Pico)__
    - If this is not displayed, but another MicroPython option is displayed, select that.
    - If no MicroPython options are displayed, remove and reattach the USB cable to the PC and try again.
0. The __Shell__ window should display "MicroPython v1.24.1" or similar.
0. Click next to the __>>>__ and type "help()", then press enter.
    - It should display "Welcome to MicroPython!".
0. The __Shell__ is an interactive prompt where python commands can be entered on line at a time.
    
    These commands will be executed immediately by the board. If the command has not been entered correctly (commonly called a __syntax error__), the shell will display a warning.
0. In the __Shell__, run the following commands, pressing __Enter__ after each one:
    
    ```
    led = machine.Pin(25, machine.Pin.OUT)
    led.high()
    ```
0. The LED should now be turned on.
0. Now enter the following commands:

    ```
    led.low()
    ```
0. The LED should now be turned off.
0. Now enter the following command:

    ```
    timer = machine.Timer(freq=1, callback=lambda t: led.toggle())
    ```
0. The LED should now be toggling between on and off once per second.