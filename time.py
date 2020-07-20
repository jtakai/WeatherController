import configparser
import requests
import sys
import time
import board
import busio
import adafruit_pca9685

from datetime import datetime
from adafruit_servokit import ServoKit

def InitSteppers():
    from adafruit_motorkit import MotorKit
    from adafruit_motor import stepper
    kit = MotorKit()
    kit.stepper1.onestep()
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    for i in range(200):
        kit.stepper1.onestep(style=stepper.MICROSTEP)

    return()

def InitServos():
    print("\n--> Initialize Servos")
    # Set channels to the number of servo channels on your kit.
    # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
    
    i2c = busio.I2C(board.SCL, board.SDA)
    kit == adafruit_pca9685.PCA9685(i2c)
    kit = ServoKit(channels=16)
    kit.servo[0].set_pulse_width_range(1000, 2000)
    kit.servo[8].set_pulse_width_range(1000, 2000)
    kit.servo[12].set_pulse_width_range(1000, 2000)

    kit.servo[0].actuation_range = 180
#    kit.servo[4].actuation_range = 180
    kit.servo[8].actuation_range = 180
    kit.servo[12].actuation_range = 180

    print("\n--> Test Servos")
    # Test ServoKit
    
    # Test Standard Servo
    kit.servo[0].angle = 180
    time.sleep(0.25)
    kit.servo[8].angle = 180
    time.sleep(2)
    kit.servo[12].angle = 180
    time.sleep(0.25)
    kit.servo[0].angle = 0
    time.sleep(0.25)
    kit.servo[8].angle = 0
    time.sleep(0.25)
    kit.servo[12].angle = 0
    time.sleep(0.25)

    
    kit.continuous_servo[4].throttle = 0

#    kit.servo[4].angle = 180

    # Test Continuous Servo
    kit.continuous_servo[4].throttle = 1
    time.sleep(1)
    time.sleep(2)
    kit.continuous_servo[4].throttle = -1
    time.sleep(1)
    kit.continuous_servo[4].throttle = -0.1
    
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
    location = "Hermosa+Beach"

    #Get the API Key for openweathermap.org
    api_key = get_api_key()
    weather = get_weather(api_key, location)
    
    print("** <",weather['main']['temp'], ">")
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
    print("\n--> Run Starting v31")

#    if len(sys.argv) != 2:
#        exit("Usage: {} LOCATION".format(sys.argv[0]))
#    location = sys.argv[1]


    #InitServos() #Initialize Servo Controller
    #InitSteppers() #Initialize Servo Controller
    #TestServos() #Reset Servos
    
    InitWeather() #Fetch Current Weather

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


