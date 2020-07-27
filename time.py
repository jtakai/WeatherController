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
from servos import InitServos
from datetime import datetime

def get_api_key():
    print("\n--> Set API Key : Weather")
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(api_key, location):
    print("\n--> Gathering Data : Weather")
    
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def InitWeather():
    print("\n--> Initialize and Read Current Weather")
    location = constant.CITY
    
    #Get the API Key for openweathermap.org
    api_key = get_api_key()
    weather = get_weather(api_key, location)
    
    print("<-----Find Temp Position--------->")
    
    # Pull Temp <temp> for Display
    tempMin = constant.TEMPMIN
    tempMax = constant.TEMPMAX
    tempDiff = tempMax - tempMin
    
    currentTemp = weather['main']['temp']
    #print("** temp <",currentTemp, ">")
        
    xTemp = currentTemp - tempMin
    percentTemp = ( xTemp / tempDiff ) * 100.0
    print("** percentTemp <",percentTemp, "%>")
    print("<-------------->")
    
    # Pull Sun Travel <range> for Arm
    # This calculates full range of 100% arm travel based on day's sun exposure
    #
    print("<-----Find Time Position--------->")
    
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
    correctPosition = percentTime * maxRange
    
    print("** correctPosition <",correctPosition, " degrees>")
    
    # lTime = localtime()
        # print("** localtime <",lTime, ">")
        
        # s = time.gmtime(0)
        # print("** Timezone <",s, ">")
    print(" ")
        
    print("<-------------->")
        
        # Full Weather Data Structure
    print("** <",weather, ">")
        #TASK: Need to return intelligent/formatted weather data for position modules
        
    return()
    
def SetSun():
    print("\n--> Setting Position : Sun")
    #TASK: Need to solve Positional math for arc position relative to Time (time-of-day)
        
    return()

def SetTemp():
    print("\n--> Setting Position : Temp")
    #TASK: Need to solve Positional math for StraightLine position
        
    return()

def SetMoon():
    print("\n--> Setting Position : Moon")
    #TASK: Need to solve Positional math for arc position relative to SkyPosition
        
    return()

def SetClouds():
    print("\n--> Setting Position : Clouds")
    #TASK: Need to solve Positional math for arc position relative to Sun (time-of-day)
        
    return()

def FlyPig():
    print("\n--> Flying the Pig!")
    #TASK: Need to solve Positional math for flight arc start/end/return/start
    #TASK: Need to solve trigger for flight and return timing
        
    return()

def GetTime():
    print("\n--> Gathering Data : GetTime")
    now = datetime.now()
    print("<", now, ">")
    current_time = now.strftime("%H:%M")
    print("** Current Time =", current_time)
    
    #TASK: Need to solve Positional math for hours:minutes
        #TASK: Need to return intelligent/formatted time data for position modules
        
    print("\n--> GetTime complete")


def main():
    print("\n--> Run Starting v40")
    
    #    if len(sys.argv) != 2:
        #        exit("Usage: {} LOCATION".format(sys.argv[0]))
        #    location = sys.argv[1]
        #    print("\n--> Playing Music")
        #    asyncio.run(InitMusic())
        
        #    InitMusic()
        
    ClearSteppers() #Initialize Stepper Controller
    
    #SmallInitServos() #Initialize Servo Controller
    #InitServos() #Initialize Servo Controller
    #TestServos() #Reset Servos
        
    InitWeather() #Fetch Current Weather
    #
    GetTime()
    
    #Let's get to work!
    SetSun()
    SetMoon()
    SetClouds()
    SetTemp()
    FlyPig()
        
    print("\n--> Run Complete")

if __name__ == '__main__':
    main()


