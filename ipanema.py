import configparser
import requests
import sys
import time
import board
import busio
import constant
import os
import asyncio


def InitMusic():
#    subprocess.Popen("play /home/pi/WeatherController/Carnival3.wav")
#    pygame.mixer.init()
#    pygame.mixer.music.load("Carnival3.wav")
#    pygame.mixer.music.play()
#    while pygame.mixer.music.get_busy() == True:
#        continue
    print("\n--> Playing Music")

#    play music track using USB Audio board
    
    os.system("aplay --device=plughw:2,0 /home/pi/WeatherController/ipanema.wav &")
#    os.system("aplay --device=plughw:2,0 /home/pi/WeatherController/fox.wav &")
#    os.system("play /home/pi/WeatherController/Carnival5short.wav &")


