import configparser
import requests
import sys
import time
import board
import busio
import constant
import os
import asyncio

from steppers import ClearSteppers
from steppers import MoveStepperSun
from steppers import MoveStepperCloud
from steppers import MoveStepperTemp
from steppers import MoveStepperFlyPig
from datetime import datetime
from datetime import date

from servos import InitServos
from gettime import GetTime

def InitMusic():
#    subprocess.Popen("play /home/pi/WeatherController/Carnival3.wav")
#    pygame.mixer.init()
#    pygame.mixer.music.load("Carnival3.wav")
#    pygame.mixer.music.play()
#    while pygame.mixer.music.get_busy() == True:
#        continue
    print("\n--> Playing Music")

#    play music track using USB Audio board
    
    os.system("aplay --device=plughw:3,0 /home/pi/WeatherController/Carnival5short.wav &")
#    os.system("play /home/pi/WeatherController/Carnival5short.wav &")


def get_api_key():
#    print("\n--> Set API Key : Weather")
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(api_key, location):
#    print("\n--> Gathering Data : Weather")
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

currentSunPosition = 0
#print("** correctPosition <",currentSunPosition, " units>")

#Get the API Key for openweathermap.org
api_key = get_api_key()
location = constant.CITY
# Full Weather Data Structure
#print("** <",weather, ">")
#TASK: Need to return intelligent/formatted weather data for position modules
#weather = get_weather(api_key, location)
#print("\n--> Initialize and Read Current Weather")
#print(weather['dt'])

def SetSun( currSunPos ):
#    print("\n--> Setting Position : Sun")
#    print(" Incoming Correct Sun Position : ", currSunPos)
    weather = get_weather(api_key, location)
#    print(weather['dt'])
#    print("** <",weather, ">")

    #TASK: Need to solve Positional math for arc position relative to Time (time-of-day)
    #############################################
    # Pull Sun Travel <range> for Arm
    # This calculates full range of 100% arm travel based on day's sun exposure
    #############################################
    #print("<-----Find Time Position--------->")
    #############################################
    #print("** Sunrise <",weather['sys']['sunrise'], ">")
    #print("** Sunset <",weather['sys']['sunset'], ">")
    timeDiff = weather['sys']['sunset'] - weather['sys']['sunrise']
#    print("** timeDiff <",timeDiff,">")
    #range = timeDiff / 3600.0
    #print("** range <",range,">")
    rawTime = weather['dt']
    rawTime = time.time()
#    print("** Time <",rawTime, ">")
    xTime = rawTime - weather['sys']['sunrise']
#    print("** xTime <",xTime, ">")
    # where are we in the percentage of the day?
    percentTime = ( xTime / timeDiff )
#    print("** percentTime <",percentTime * 100, ">")
    #correctPosition establishes the range position between 0->[maxRange]] degrees
    maxRange = constant.ARM_MAX_RANGE # currently set to 180 degrees
#    print("** maxRange <",maxRange, ">")
    x = int(percentTime * maxRange - currSunPos)
    y = int(percentTime * maxRange)
#    print("** differential moving ---> ", x, " units")
    if x > 0:
        print("####################################################")
    else:
        print("#")

    MoveStepperSun(x)
    # lTime = localtime()
    # print("** localtime <",lTime, ">")
    # s = time.gmtime(0)
    # print("** Timezone <",s, ">")
    #############################################
#    print(" Returning : ", y)

    return y

def SetTemp():
    print("\n--> Setting Position : Temp")
    #TASK: Need to solve Positional math for StraightLine position
    weather = get_weather(api_key, location)
    #############################################
    # Pull Temp <range> for Arm
    # This calculates full range of 100% arm travel based on current temp + full range defined
    #############################################
    #print("<-----Find Temp Position--------->")
    #############################################
    # Pull Temp <temp> for Display
    tempMin = constant.TEMPMIN
    tempMax = constant.TEMPMAX
    tempDiff = tempMax - tempMin
    currentTemp = weather['main']['temp']
    #print("** temp <",currentTemp, ">")
    xTemp = currentTemp - tempMin
    percentTemp = int(( xTemp / tempDiff ) * 100.0)
    print("** percentTemp <",percentTemp, "%>")
    MoveStepperTemp(percentTemp)
    return()

def SetMoon():
    print("\n--> Setting Position : Moon")
    #TASK: Need to solve Positional math for arc position relative to SkyPosition
    return()

def SetClouds():
#    print("\n--> Setting Position : Clouds")
    #TASK: Need to solve Positional math for arc position relative to Sun (time-of-day)
#    print("\n--> Setting Position : Sun")
    #TASK: Need to solve Positional math for arc position relative to Time (time-of-day)
    weather = get_weather(api_key, location)
    #############################################
    # Pull Sun Travel <range> for Arm
    # This calculates full range of 100% arm travel based on day's sun exposure
    #############################################
    #print("<-----Find Time Position--------->")
    #############################################
    #print("** Sunrise <",weather['sys']['sunrise'], ">")
    #print("** Sunset <",weather['sys']['sunset'], ">")
    timeDiff = weather['sys']['sunset'] - weather['sys']['sunrise']
    #print("** timeDiff <",timeDiff,">")
    #range = timeDiff / 3600.0
    #print("** range <",range,">")
    rawTime = weather['dt']
    #print("** Time <",rawTime, ">")
    xTime = rawTime - weather['sys']['sunrise']
    #print("** xTime <",xTime, ">")
    # where are we in the percentage of the day?
    percentTime = ( xTime / timeDiff )
    #print("** percentTime <",percentTime, ">")
    #correctPosition establishes the range position between 0->[maxRange]] degrees
    maxRange = constant.ARM_MAX_RANGE # currently set to 180 degrees
    correctPosition = int(percentTime * maxRange)
#    print("** correctPosition <",correctPosition, " units>")
    MoveStepperCloud(correctPosition)
    # lTime = localtime()
    # print("** localtime <",lTime, ">")
    # s = time.gmtime(0)
    # print("** Timezone <",s, ">")
    #############################################
    return()

def FlyPig():
    print("\n--> Flying the Pig!")
    MoveStepperFlyPig()
    #TASK: Need to solve Positional math for flight arc start/end/return/start
    #TASK: Need to solve trigger for flight and return timing
    return()

def main():
    print("\n--> Run Starting v45")
    #    if len(sys.argv) != 2:
    #        exit("Usage: {} LOCATION".format(sys.argv[0]))
    #    location = sys.argv[1]
    #    asyncio.run(InitMusic())
        
#    InitMusic()
#    time.sleep(10) #Wait until the chain/ratchet sound plays before launching the motors

    ClearSteppers() #Initialize Stepper Controller
    #SmallInitServos() #Initialize Servo Controller
    #InitServos() #Initialize Servo Controller
    #TestServos() #Reset Servos
    #GetTime() #Get Systime
    counter = 0
    z = 0
    currentSunPosition = 0

    while (1):
        #Let's get to work!
        print(" Calling SetSun with : ", z)

# Stepper 1
        z = SetSun(currentSunPosition)
        currentSunPosition = z
        print(" Correct Sun Position : ", currentSunPosition)
        time.sleep(1)

# Stepper 2
        SetTemp()
        time.sleep(1)
        
# Stepper 3
        SetClouds()
        time.sleep(1)

# Stepper 4
        FlyPig()
        
        
        #SetMoon()
        counter = counter + 1
        print("Run number ",counter)
        print("\n--> Run Complete")
        time.sleep(60 * 5)


if __name__ == '__main__':
    main()

