from sense_hat import SenseHat
from sense_emu import SenseEmu
from time import sleep

# FLAGS!!
# Feel free to change this however you want! >~<

use_emu_sense = False # this uses the emu sense app for the pi
use_Celelis = False # For people who live outside the US


sense = SenseHat()

if use_emu_sense == True:
    sense = SenseEmu

# the preload
sense.clear()
sense.show_message("Now loading....")

# the real load

emotion = "Happy"
# Buddy can have differnt emotions
# Happy, Hungry, Cold, Hot, waterly

def CelelisToFahrenheit(input):
    output = input * 1.8
    output = output + 32
    return output