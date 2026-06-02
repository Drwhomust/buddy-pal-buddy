from sense_hat import SenseHat
from time import sleep
import math
import atexit

# -------------------------------------------------------------------
# FLAGS!!
# Feel free to change this however you want! >~<

use_emu_sense = True # this uses the emulator sense app for the pi
use_Low_Power_Mode = False # this dims the light to use less power
round_up_temp = True # rounds up the temp value to the nearest number (no deicamls)
show_Hints = True # I will tell you what I want though the debug logs

# -------------------------------------------------------------------

# the rest is code:

if use_emu_sense:
    from sense_emu import SenseHat
else:
    from sense_hat import SenseHat

sense = SenseHat()

# the preload
sense.clear()

if use_Low_Power_Mode:
    sense.low_light = True
else:
    sense.low_light = False

sense.show_message("Now loading....")

# the real load

emotion = "Happy"
# Buddy can have differnt emotions
# Happy, Hungry, Cold, Hot
# all do what they do from their name

# functions that might be needed!

def CelelisToFahrenheit(input):
    output = input * 1.8
    output = output + 32
    if round_up_temp: # if it rounds it rounds. else it skips!
        output = math.ceil(output)
    return output

def exit_Clean_Up():
    sense.show_message("Goodbye! :)")
    sense.clear()

def temp_Check(temputer):
    if temputer >= 95:
        emotion = "Hot"
        if show_Hints:
            print("I am way too hot! Cool me down!")

    if temputer <= 68:
        emotion = "Cold"
        if show_Hints:
            print("I am too cold! Warm me up!")

# variables!

hunger = 100 # how hungery they get

temp = CelelisToFahrenheit(sense.get_temperature()) # get's init temp


print(temp)

atexit.register(exit_Clean_Up)

# This is the color pattle for the defult face (aka buddy themselves)

X = [255,255,255] # White
O = [42,161,252] # The Blue
C = [42,88,252] # the eyes and mouth
R = [255,0,0] # red for heat
B = [116,184,252] # cold sweats

# Faces!

happy_face = [
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, O, C, X, X, X, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, X, O, C, C, C, O, X,
]

blink = [
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, X, X, X, X, O,
    X, O, X, X, X, X, X, O,
    X, O, C, C, C, C, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, X, O, C, C, C, O, X,
]

while True:
    sense.set_pixels(happy_face)
    sleep(1)
