from sense_hat import SenseHat
from time import sleep
import math
import atexit
import random

# -------------------------------------------------------------------
# FLAGS!!
# Feel free to change this however you want! >~<

use_emu_sense = False # this uses the emulator sense app for the pi
use_Low_Power_Mode = False # this dims the light to use less power
round_up_temp = True # rounds up the temp value to the nearest number (no deicamls)
show_Hints = True # I will tell you what I want though the debug logs. Also good for debugging lolz
use_custom_buddy = False # This makes it where you can use a custom buddy. a 8x8 image for each emotion with a charater of your choice!
custom_buddy_path = "./image/" # the folder where all the image data is stored
# by defult the custom image path is the image folder of the github repo.
# feel free to change it to your path or use the images in that folder
# as a reference when making your own custom charater

# also the charater in there as a refernce is my OC timbo
# a nightcrawler from the roblox game kaiju paradise

# -------------------------------------------------------------------

# the rest is code:

if use_emu_sense:
    from sense_emu import SenseHat
else:
    from sense_hat import SenseHat

sense = SenseHat()

# the preload
sense.clear()

# does low power = true???
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

def exit_Clean_Up(): # the clean up function
    sense.clear() # clears everything
    sense.show_message("Goodbye! :)") # says final goodbye
    sense.clear() # clears for the next program

def wakey_wakey(open_eyes, closed_eyes):
    if use_custom_buddy:
        sense.load_image(custom_buddy_path + "blink.png")
    else:
        sense.set_pixels(closed_eyes)
    
    sleep(2.5) # waiting for the buddy to wake up

    if use_custom_buddy:
        sense.load_image(custom_buddy_path + "happy.png")
    else:
        sense.set_pixels(open_eyes)

def set_pixel_via_image(emo):
    # checks if you can use custom buddies
    if use_custom_buddy:
        # what emotion
        if emo == "Happy":
            sense.load_image(custom_buddy_path + "happy.png")
        else:
            if emo == "Hungry":
                sense.load_image(custom_buddy_path + "hungery.png")
            else:
                if emo == "Cold":
                    sense.load_image(custom_buddy_path + "cold.png")
                else:
                    if emo == "Hot":
                        sense.load_image(custom_buddy_path + "hot.png")
                    else:
                        if emo == "blink":
                            sense.load_image(custom_buddy_path + "blink.png")

def force_face_load(face):
    sense.set_pixels(face)
                
def get_temp():
    output = CelelisToFahrenheit(sense.get_temperature())
    return output

# variables!

hungery = 100 # how hungery they get

lives = 3 # how many lives before buddy dies

time = 0 # helps counts the secounds of time passed!

atexit.register(exit_Clean_Up)

# This is the color pattle for the defult face (aka buddy themselves)

X = [255,255,255] # White
O = [42,161,252] # The Blue
C = [42,88,252] # the eyes and mouth
R = [255,0,0] # red for heat
B = [116,184,252] # cold sweats

# Faces!
# for the defelt

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

blink = [ # this is also used for dead face since it's eyes is closed
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, X, X, X, X, O,
    X, O, X, X, X, X, X, O,
    X, O, C, C, C, C, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, X, O, C, C, C, O, X,
]

hot_face = [
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, R, R, R, X, O,
    X, O, C, X, R, R, C, O,
    X, O, C, X, X, R, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, X, O, C, C, C, O, X,
]

cold_face = [
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, B, B, B, X, O,
    X, O, C, X, B, B, C, O,
    X, O, C, X, X, B, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, X, O, C, C, C, O, X,
]

hungery_face = [
    X, X, X, X, X, X, X, X,
    X, X, O, O, O, O, O, X,
    X, O, X, X, X, X, X, O,
    X, O, C, X, X, X, C, O,
    X, O, C, X, X, X, C, O,
    X, O, X, X, X, X, X, O,
    X, O, C, C, C, C, C, O,
    X, X, O, O, O, O, O, X,
]


# logic

wakey_wakey(happy_face, blink) # wakes up

def feed():
    global hungery
    if hungery <= 100:
        hungery = hungery + 5
        if show_Hints:
            print("I am eating :D")
    
    if hungery > 100:
        hungery = 100
        if show_Hints:
            print("I am full!")

sense.stick.direction_any = feed

while True:

    # checks if they ran out of lives
    if lives <= 0:
        sense.clear()
        sense.show_message("You lost :(")
        exit()
    
    # get's random number for random event
    random_numberz = random.randint(1,100)

    # get temp
    temp = get_temp()

    if temp > 110:
        if show_Hints:
            print("I am too hot")

        emotion = "Hot"
    else:
        if temp < 68:
            if show_Hints:
                print("I am too cold!")
    
            emotion = "Cold"

    # blinks
    if random_numberz <= 10:
        if use_custom_buddy:
            set_pixel_via_image("Blink")
            sleep(0.9)
            set_pixel_via_image(emotion)
        else:
            sense.set_pixels(blink)
            sleep(0.9)
            sense.set_pixels(happy_face)

    # handles making buddy go hungery
    if random_numberz > 50:
        hungery = hungery - 5
        if show_Hints:
            print("Just lost some hunger. Now at...")
            print(hungery)

    # tells the player then they are hungery
    if hungery < 50:
        if show_Hints:
            print("I am hungery now...")
        
        emotion = "Hungry"

    if hungery >= 100:
        if show_Hints:
            print("I am full now!")
        
        emotion = "Happy"

    if hungery <= 0:
        lives = lives - 1
        hungery = 100
        if show_Hints:
            print("I lost a life due to being too hungery. you are at")
            print(lives)
            print("lives")

    if use_custom_buddy:
        set_pixel_via_image(emotion)
    else:
        if emotion == "Happy":
            sense.set_pixels(happy_face)
        else:
            if emotion == "Cold":
                sense.set_pixels(cold_face)
            else:
                if emotion == "Hot":
                    sense.set_pixels(hot_face)
                else:
                    if emotion == "Hungry":
                        sense.set_pixels(hungery_face)

    if time == 60:
        if time == 60 and emotion in ["Cold", "Hot"]:
            lives = lives - 1
            time = 0
            if show_Hints:
                print("I lost a life dut to being too " + emotion)
                print("I now have this many lives")
                print(lives)

    
    sleep(1)
    time = time + 1

