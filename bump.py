import configparser
import requests
import sys
import time
import board
import busio
import adafruit_pca9685
import constant
import os
import asyncio

from datetime import datetime
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

if len(sys.argv) != 2:
	exit("Usage: {} LOCATION".format(sys.argv[0]))

rotations = int(sys.argv[1])

print(rotations)

kit = MotorKit()
kit1 = MotorKit(address=0x61)

for i in range(rotations):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    time.sleep(0.01)


    
kit.stepper1.release()
kit1.stepper1.release()

