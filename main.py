from sense_hat import SenseHat
from sense_emu import SenseEmu
from time import sleep

# -------------------------------------------------------------------
# FLAGS!!
# Feel free to change this however you want! >~<

use_emu_sense = False # this uses the emulator sense app for the pi
use_Celelis = False # For people who live outside the US
use_Low_Power_Mode = False # this dims the light to use less power

# -------------------------------------------------------------------

sense = SenseHat()

if use_emu_sense == True:
    sense = SenseEmu

# the preload
sense.clear()

if use_Low_Power_Mode == True:
    sense.low_light = True
else:
    sense.low_light = False

sense.show_message("Now loading....")

# the real load

# functions that might be needed!
def CelelisToFahrenheit(input):
    output = input * 1.8
    output = output + 32
    return output

# variables!

emotion = "Happy"
# Buddy can have differnt emotions
# Happy, Hungry, Cold, Hot, waterly
# all do what they do from their name

hunger = 100 # how hungery they get

temp = CelelisToFahrenheit(sense.get_temperature) # get's init temp

if temp >= 95:
    emotion = "Hot"
else:
    if temp <= 68:
        emotion = "Cold"

print(temp)

# This is the color pattle for the defult face (aka buddy themselves)

X = [255,255,255] # White
O = [42,161,252] # The Blue
C = [42,88,252] # the eyes and mouth

# Faces!

happy_face = [
    X, X, X, X, X, X, X,
    X, X, O, O, O, X, X,
    X, O, C, X, C, O, X,
    X, O, C, X, C, O, X,
    X, O, X, X, X, O, X,
    X, O, C, X, C, O, X,
    X, O, C, C, C, O, X,
    X, X, O, O, O, X, X,
]

sense.set_pixels(happy_face)