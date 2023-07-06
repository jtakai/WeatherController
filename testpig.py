import configparser
import requests
import sys
import time
import board
import busio
import constant
import os
import asyncio

from datetime import datetime
from datetime import date
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

from servos import InitServos
from gettime import GetTime
from music import InitMusic

def main():
    kit = MotorKit()
    kit1 = MotorKit(address=0x61)

    kit.stepper1.release()
    kit.stepper2.release()
    kit1.stepper1.release()
    kit1.stepper2.release()

    dist = constant.ARM_MAX_RANGE * constant.TIME_MULTIPLIER
    
    
    for i in range(dist):
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
    time.sleep(0.5)
    for i in range(dist):
        kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
        
    kit.stepper1.release()
    kit.stepper2.release()
    kit1.stepper1.release()
    kit1.stepper2.release()

if __name__ == '__main__':
    main()

