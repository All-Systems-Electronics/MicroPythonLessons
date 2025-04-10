from machine import Pin, PWM
import time

# Timer class used for checking how much time has passed.
class ElapsedMS:
    def __init__(self):
        self.last_time_ = self.get_time()

    def restart(self):
        self.last_time_ = self.get_time()

    def has_elapsed(self, ms: int):
        if (self.get_time() - self.last_time_) >= ms:
            return True
        return False

    def has_elapsed_restart(self, ms: int):
        if self.has_elapsed(ms):
            self.restart()
            return True
        return False

    def get_time(self) -> int:
        return time.ticks_ms()

# Manages the flashing of an LED in the background.
class Heartbeat():
    def __init__(self, set_state):
        self.set_state = set_state
        self.set_state(False)
        self.state = False
        self.elapsed = ElapsedMS()

    def update(self):
        if self.elapsed.has_elapsed_restart(1000):
            self.state = not self.state
            self.set_state(self.state)

# Debounces an input.
class Debounce:
    def __init__(self, initial_state = False, debounce_time = 50):
        self.state_ = initial_state
        self.debounce_time_ = debounce_time
        self.elapsed_ = ElapsedMS()

    def update(self, new_state):
        if new_state != self.state_:
            if self.elapsed_.has_elapsed_restart(self.debounce_time_):
                self.state_ = new_state
        else:
            self.elapsed_.restart()

    def state(self):
        return self.state_

# Debounces an input and then uses the debounced state to determine the state of the button.
# Allows the caller to check for different events that may have occurred on the button.
class Button:
    def __init__(self, get_state):
        self.get_state_ = get_state
        self.pressed_ = False
        self.last_pressed_ = False
        self.debounced_state_ = Debounce()
        self.pressed_timer_ = ElapsedMS()

    def update(self):
        self.last_pressed_ = self.pressed_
        self.debounced_state_.update(self.get_state_())
        self.pressed_ = self.debounced_state_.state()
        if self.just_pressed():
            self.pressed_timer_.restart()

    def is_pressed(self):
        return self.pressed_

    def is_released(self):
        return not self.pressed_

    def just_changed(self):
        return self.pressed_ != self.last_pressed_

    def just_pressed(self):
        return self.just_changed() and self.is_pressed()

    def just_released(self):
        return self.just_changed() and self.is_released()

    def is_held(self, hold_time_ms):
        return self.is_pressed() and self.pressed_timer_.has_elapsed(hold_time_ms)

    def restart_held(self):
        self.pressed_timer_.restart()

# A theme is a list of tuple[int,int]
# The first item in the tuple is the frequency.
# The second item in the tuple is the milliseconds.

QUAVER = 350
SEMI_QUAVER = 150

# Note definitions can be found here:
# https://github.com/bhagman/Tone/blob/master/Tone.h
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_G5 = 783
NOTE_B4 = 493
NOTE_D5 = 587
NOTE_GS5 = 830
NOTE_A5 = 880
NOTE_AS5 = 932
NOTE_B5 = 987
NOTE_C6 = 1046
NOTE_D6 = 1174
NOTE_DS6 = 1244
NOTE_E6 = 1318

# Plays all the notes in a sequence, based on the timing given in the sequence.
class TunePlayer:
    STATE_PLAY_NOTE = 0
    STATE_PAUSE = 1
    STATE_FINISHED = 2
    STATE_SIZE = 3

    PAUSE_TIME = 50

    # set_freq must be a callable that takes an int and returns None
    def __init__(self, set_freq, theme: list[tuple[int, int]]):
        self.set_freq = set_freq
        self.theme = theme
        self.elapsed = ElapsedMS()
        self.index = 0
        self.state = self.STATE_PLAY_NOTE
        self.last_state = self.STATE_SIZE

    def update(self):
        first_time = self.state != self.last_state
        self.last_state = self.state

        if self.state == self.STATE_PLAY_NOTE:
            if first_time:
                self.elapsed.restart()
                self.set_freq(self.theme[self.index][0])

            if self.elapsed.has_elapsed_restart(self.theme[self.index][1]):
                self.index += 1
                self.state = self.STATE_PAUSE
        elif self.state == self.STATE_PAUSE:
                if first_time:
                    self.elapsed.restart()
                    self.set_freq(0)
                if self.elapsed.has_elapsed_restart(self.PAUSE_TIME):
                    if self.index >= len(self.theme):
                        self.state = self.STATE_FINISHED
                    else:
                        self.state = self.STATE_PLAY_NOTE

    def is_finished(self):
        return self.state == self.STATE_FINISHED

# The opening few notes of "Mary had a Little Lamb"
TUNE = [
    (NOTE_E5, QUAVER),
    (NOTE_D5, QUAVER),
    (NOTE_C5, QUAVER),
    (NOTE_D5, QUAVER),
    (NOTE_E5, QUAVER),
    (NOTE_E5, QUAVER),
    (NOTE_E5, QUAVER),
]

def beep(freq: int):
    if freq < 100:
        # Turn the beeper off by setting a default frequency and a duty cycle of 0.
        beeper_pwm.freq(5000)
        beeper_pwm.duty_u16(0)
    else:
        # Set the frequency desired by the caller.
        beeper_pwm.freq(freq)
        # Set the duty cycle to 50%, where 65535 is the maximum possible value.
        beeper_pwm.duty_u16(int(65535 / 2))

# Main script execution starts here
print(f"#####Lesson6#####")

button_input = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
button = Button(lambda: not button_input.value())
led = Pin(20, mode=Pin.OUT, value=0)
heartbeat_led = Pin(25, mode=Pin.OUT, value=0)
heartbeat = Heartbeat(lambda value: heartbeat_led.value(value))
beeper_pwm = PWM(Pin(15))
beeper_pwm.duty_u16(0)
tune_player = TunePlayer(lambda freq: beep(freq), TUNE)
playing_tune = False
waiting_for_release = False

while True:
    heartbeat.update()
    button.update()
    
    if button.is_held(1000) and not playing_tune:
        tune_player = TunePlayer(lambda freq: beep(freq), TUNE)
        playing_tune = True
        waiting_for_release = True
    elif button.just_released():
        if waiting_for_release:
            waiting_for_release = False
        else:
            led.toggle()
            playing_tune = False
            beep(0)
        
    if playing_tune:
        tune_player.update()
        if tune_player.is_finished():
            playing_tune = False

