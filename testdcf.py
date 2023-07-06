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
    #kit = MotorKit()
    kit1 = MotorKit(address=0x61)

    #kit.stepper1.release()
    
    #Door
    #kit.stepper2.release()
    
    #kit1.stepper1.release()
    #kit1.stepper2.release()

    #dist = constant.OPENDOOR
    
    #for i in range(dist):
    #   kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    #    time.sleep(constant.MOTOR_SPEED)
    kit1.motor1.throttle = constant.DCMOTORSPEED
    kit1.motor2.throttle = constant.DCMOTORSPEED
    kit1.motor3.throttle = constant.DCMOTORSPEED

    time.sleep(constant.TEMPSLIDE *2)

    kit1.motor1.throttle = 0.0
    kit1.motor2.throttle = 0.0
    kit1.motor3.throttle = 0.0



if __name__ == '__main__':
    main()

