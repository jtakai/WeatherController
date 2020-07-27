import configparser
import requests
import sys
import time
import board
import busio
import adafruit_pca9685
import constant
import pygame
import os

from datetime import datetime
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


def InitMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Carnival3.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def InitSteppers():
    print("\n--> Initialize Steppers")

    kit = MotorKit()
    kit1 = MotorKit(address=0x61)

    for i in range(50):
        kit.stepper1.onestep(style=stepper.DOUBLE)
        time.sleep(0.01)

    for i in range(50):
        kit1.stepper1.onestep(style=stepper.DOUBLE)
        time.sleep(0.01)

#    for i in range(200):
#        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#        time.sleep(0.01)
    
    for i in range(50):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        time.sleep(0.01)

    for i in range(50):
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        time.sleep(0.01)

    return()

def InitSteppers2():
    print("\n--> Initialize Steppers")

    kit = MotorKit()
    kit1 = MotorKit(address=0x61)

    kit.stepper1.onestep()
    time.sleep(0.1)

    for i in range(100):
        kit.stepper1.onestep(style=stepper.DOUBLE)
        kit1.stepper1.onestep(style=stepper.DOUBLE)
        time.sleep(0.01)

    for i in range(100):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(0.01)

    for i in range(100):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)

    for i in range(100):
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    
    kit.stepper1.release()
    kit1.stepper1.release()

    return()

def InitServos():
    print("\n--> Initialize Servos")
    from adafruit_servokit import ServoKit

    kit = ServoKit(address=0x44, channels=16)

    kit.servo[8].angle = 180
    kit.continuous_servo[12].throttle = 1
    time.sleep(0.25)
    kit.continuous_servo[12].throttle = -1
    time.sleep(0.25)
    kit.servo[8].angle = 0
    kit.continuous_servo[12].throttle = -0.1
        
    #kit.servo[0].set_pulse_width_range(1000, 2000)
    #kit.servo[0].actuation_range = 180
        
    print("\n--> Test Servos")
    # Test ServoKit
    kit.servo[0].angle = 180
    time.sleep(0.25)
    kit.servo[8].angle = 180
    time.sleep(0.25)
    kit.servo[4].angle = 180
    time.sleep(0.25)
    kit.servo[0].angle = 0
    time.sleep(0.25)
    kit.servo[8].angle = 0
    time.sleep(0.25)
    kit.servo[4].angle = 0
    time.sleep(0.25)
    
    # Test Continuous Servo
    kit.continuous_servo[12].throttle = 0
    kit.continuous_servo[12].throttle = 1
    time.sleep(0.25)
    kit.continuous_servo[12].throttle = -1
    time.sleep(0.25)
    kit.continuous_servo[12].throttle = -0.1

    return()

def SmallInitServos():
    print("\n--> Initialize Servos")
    from adafruit_motorkit import MotorKit
    #Initialise the first hat on the default address
    #i2c = busio.I2C(board.SCL, board.SDA)
    kit = MotorKit()
    #kit1 = MotorKit(address=0x64)
    #kit1 == adafruit_pca9685.PCA9685(i2c)
    #kit1 = ServoKit(channels=16)

    for i in range(300):
        kit.stepper1.onestep()
        time.sleep(0.01)

    return()
    
def TestServos():
    print("\n--> Test Servos")
    # Test ServoKit
    
    # Test Standard Servo
    #kit.servo[0].angle = 180
    #kit.servo[0].angle = 0
    
    # Test Continuous Servo
    #kit.continuous_servo[1].throttle = 1
    #time.sleep(1)
    #kit.continuous_servo[1].throttle = -1
    #time.sleep(1)
    #kit.continuous_servo[1].throttle = 0
    return()

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
    print("\n--> Run Starting v33")
    
    os.system("play /home/pi/WeatherController/Carnival3.wav &")

    GetTime()
    SetSun()



    SetMoon()
    SetClouds()
    SetTemp()
    FlyPig()
    
    print("\n--> Run Complete")

if __name__ == '__main__':
    main()


