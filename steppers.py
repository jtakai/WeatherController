import time
import constant

from datetime import datetime
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()
kit1 = MotorKit(address=0x61)

def ReleaseSteppers():
    kit.stepper1.release()
    kit1.stepper1.release()
    kit1.stepper2.release()
    return constant.TRUE


def ClearSteppers():
    print("\n--> Initialize Steppers")
        
    for i in range(200):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        kit1.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        time.sleep(0.01)

    for i in range(200):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        kit1.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        kit1.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(0.01)

    state = ReleaseSteppers()
    
    if state == constant.FALSE:
        print("Stepper Release Failed")
    else:
        print("Stepper Release Success")

    
    return()
    
