import time
import constant

from datetime import datetime
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()
kit1 = MotorKit(address=0x61)


def MoveStepperFlyPig():
    print("\n--> Flying Pig")
    dist = 100 * constant.TIME_MULTIPLIER
    for i in range(dist):
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
    for i in range(dist):
        kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
        
    state = ReleaseSteppers()
    return()

def MoveStepperSun(measurement):
    print("\n--> Move Stepper Time")
    dist = measurement * constant.TIME_MULTIPLIER
    for i in range(dist):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
    state = ReleaseSteppers()
    return()

def MoveStepperCloud(measurement):
    print("\n--> Move Stepper Cloud")
    dist = measurement * constant.TIME_MULTIPLIER
    for i in range(dist):
        kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
    state = ReleaseSteppers()
    return()

def MoveStepperTemp(measurement):
    print("\n--> Move Stepper: Temperature")
    dist = measurement * constant.TEMP_MULTIPLIER

    for i in range(dist):
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(constant.MOTOR_SPEED)
    state = ReleaseSteppers()
    return()


def ReleaseSteppers():
    kit.stepper1.release()
    kit.stepper2.release()
    kit1.stepper1.release()
    kit1.stepper2.release()
    #    if state == constant.FALSE:
    #        print("Stepper Release Failed")
    #    else:
    #        print("Stepper Release Success")

    return constant.TRUE


def ClearSteppers():
    print("\n--> Initialize Steppers")
        
    for i in range(constant.ARM_MAX_RANGE):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.01)

    for i in range(constant.ARM_MAX_RANGE):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)

    state = ReleaseSteppers()
    
    if state == constant.FALSE:
        print("Stepper Release Failed")
    else:
        print("Stepper Release Success")
    
    return()
    
