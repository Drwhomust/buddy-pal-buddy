from sense_hat import SenseHat
from sense_emu import SenseEmu
from time import sleep

# FLAGS!!
# Feel free to change this however you want! >~<

use_emu_sense = False # this uses the emu sense app for the pi


sense = SenseHat()

if use_emu_sense == True:
    sense = SenseEmu

# the preload
sense.clear()
sense.show_message("Now loading....")

# the real load

