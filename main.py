from sense_hat import SenseHat
from time import sleep
import math
import atexit

# -------------------------------------------------------------------
# FLAGS!!
# Feel free to change this however you want! >~<

use_emu_sense = False # this uses the emulator sense app for the pi
use_Celelis = False # For people who live outside the US
use_Low_Power_Mode = False # this dims the light to use less power
round_up_temp = True # rounds up the temp value to the nearest number (no deicamls)

# -------------------------------------------------------------------

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

# variables!

emotion = "Happy"
# Buddy can have differnt emotions
# Happy, Hungry, Cold, Hot, waterly
# all do what they do from their name

hunger = 100 # how hungery they get

temp = CelelisToFahrenheit(sense.get_temperature()) # get's init temp

if temp >= 95:
    emotion = "Hot"
else:
    if temp <= 68:
        emotion = "Cold"

print(temp)

atexit.register(exit_Clean_Up)

# This is the color pattle for the defult face (aka buddy themselves)

X = [255,255,255] # White
O = [42,161,252] # The Blue
C = [42,88,252] # the eyes and mouth

# Faces!

happy_face = [
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, O, C, X, X, X, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, C, O, O,
    X, X, O, C, C, O, X, X,
]

while True:
    sense.set_pixels(happy_face)
    sleep(1)