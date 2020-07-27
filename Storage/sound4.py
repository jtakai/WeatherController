import time
import RPi.GPIO as GPIO
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Remember the current and previous button states
current_state = True
prev_state = True

# Load the sounds
sound = mixer.Sound("/home/pi/WeatherController/applause-1.wav")

sound.play()
