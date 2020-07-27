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
import asyncio

from datetime import datetime
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

def InitSteppers2():
    print("\n--> Initialize Steppers")
    kit = MotorKit()
    kit1 = MotorKit(address=0x61)
    
    
    #    kit.stepper1.onestep()
    #    time.sleep(0.1)
    
    counter0 = 0
    counter1 = 0
    
    print("counter0 = ", counter0)
    print("counter1 = ", counter1)
    
    for i in range(100):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
        counter0 = counter0 + 1
        counter1 = counter1 - 1
    
    print("counter0 = ", counter0)
    print("counter1 = ", counter1)
    
    for i in range(100):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(0.01)
        counter0 = counter0 + 1
        counter1 = counter1 - 1
    
    print("counter0 = ", counter0)
    print("counter1 = ", counter1)
    
    for i in range(100):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
        counter0 = counter0 + 1
    
    print("counter0 = ", counter0)
    print("counter1 = ", counter1)
    
    for i in range(100):
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
        counter1 = counter1 - 1
    
    print("counter0 = ", counter0)
    print("counter1 = ", counter1)
    
    print("---> NOW RESET STEPPERS ---<")

    print("counter0 = ", counter0)
    print("counter1 = ", counter1)

    for i in range(counter0):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(0.01)
        counter0 = counter0 - 1
        
    print("counter0 = ", counter0)
    print("counter1 = ", counter1)

    for i in range(-counter1):
        kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        time.sleep(0.01)
        counter1 = counter1 + 1
    print("---> STEPPERS ARE RESET ---<")

    print("counter0 = ", counter0)
    print("counter1 = ", counter1)
    
    kit.stepper1.release()
    kit1.stepper1.release()
    
    return()
    
def main():
    print("\n--> Test Run Starting v36")
    
    InitSteppers2() #Initialize Stepper Controller
    print("\n--> Test Run Complete")

if __name__ == '__main__':
    main()


