


# Lesson 2
This lesson will show how to create your first program and run it on the Pico.

1. Ensure that the Pico is connected to the PC, and that Thonny is running with the Pico selected in the bottom-right corner.
0. On the left of Thonny, there should be a window with the title __Raspberry Pi Pico__ or similar. This shows all the files that are on the connected device.
0. Right-click in Pico window and select __New File__.
0. Enter __Lesson2.py__ as the filename.
    - A new tab will be created with the desired filename, however it won't be saved to the Pico until some text is entered and the file is saved.
0. This new file is called a python script. When we tell the Pico to run it, there is a program on the Pico that reads the script and runs the program.
0. In the __Code Editor__ (in the middle of the screen, showing the filename at the top), type the following:
    
    ```
    from machine import Pin

    led = Pin(25, mode=Pin.OUT, value=0)
    ```
    - This code creates a Pin object and stores it in a new variable called led.
    - This new led variable represents what we call a pin on the MicroProcessor.
    - We have configured pin 25 to be a digital output, and set its value to 0.
    - Digital outputs (and digital inputs) can only have the values 0 or 1.
0. Save the file (CTRL+S or File->Save).
0. Press the Green __Run__ button at the top of Thonny to run the script.
0. The LED should now be turned off.
0. Change "value=0" to "value=1" and re-run the script.
    - To re-run the script, press __Stop__ at the top of Thonny.
    - Save the current file.
    - Then press __Run__ again.
        - If a script is currently running when save is attempted you may get an error.
0. The LED should now be turned on.
0. At the bottom of the file add the following:

    ```
    while True:
        led.value(0)
        led.value(1)
    ```
    - This creates a loop that will run forever, toggling the LED on and off.
    - Because we previously stored the Pin object in a variable called led, we are able to change the value of the pin using the led variable.
0. Try running this program. You should see that the LED is on, but it may not be as bright as it was before.
    - This is because it toggling on and off very quickly.
    - To slow it down, we need to add some delays.
0. At the top of the file add the following line to import the time module:
    
    ```
    import time
    ```
0. At the bottom of the file modify the while loop to look like this:

    ```
    while True:
        led.value(0)
        time.sleep_ms(1000)
        led.value(1)
        time.sleep_ms(1000)
    ```
0. The LED should now be toggling on and off every second.
0. In Python, indentation is very important.
    - In the above example, after "while True:", the following 4 lines are indented by 4 spaces.
    - This tells Python that these 4 lines are to be run as part of the while loop.
    - If the indentation is incorrect in Python, the program will either not run, or it won't run as expected.
0. We can also add some print statements to our script so we can see what part of the code is executing.
    - In the loop, try adding the following code just after setting the led value to 0. Also add it after setting the led value to 1.

        ```
        print(f"The LED value is {led.value()}")
        ```
    - After re-running the script, you should see the state of the LED printed everytime it toggles.
    - The print() function prints text to the Shell. The letters between the quotes are the string that should be printed.
    - In the above example, we have put the letter __f__ before the string. This tells python that the string may contain formatted data.
    - In this case, we want to print a value, which we put inside the {} curly braces.

We now know how to do the following:
- Create a script file on our Pico board.
- Run the script.
- Configure a Pin and toggle it in a loop.
- Print data to the Shell.