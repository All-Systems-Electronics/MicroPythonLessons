# Lesson 6
This lesson will show how to bring all the different bits of code together:
- Flashing the onboard LED to tell us the code is running.
- Reading the button input, debouncing it, and checking for different button events.
- Using the button to either toggle the external LED or play a tune if the button is held.

The circuit can be setup exactly as it was for [Lesson 5](../Lesson5/README.md).

In Thonny, copy the code from [Lesson6.py](./Lesson6.py) into Lesson6.py on the Pico.

You will see that the code is split up into different classes.
Normally each class would be in its own .py file. However, for ease of copying it onto the Pico its all in a single file.

The biggest change in this code is that we need to handle lots of different events in parallel. In previous lessons we were only doing one thing at a time, so we could just sleep for 500ms and it would work fine.

However, now that we need to do multiple things in parallel, we need to break the functionality up into classes, and use an elapsed timer class to help us manage events.

The main code is found near the bottom of the file.
Here we initialise the circuit, create objects from the classes defined higher up, and then start running our main loop.

The main loop updates all of the objects that need updating, and then checks for button presses.
- If the button is pressed and released quite quickly, it toggles the LED.
- If the button is pressed and held for more than 1 second, it starts playing the tune.
- Pressing and releasing the button again cancels the tune.