"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
 
kit.servo[0].angle = 180
kit.servo[8].angle = 180
kit.servo[12].angle = 180

time.sleep(1)
kit.servo[0].angle = 170
time.sleep(1)
kit.servo[0].angle = 45
kit.servo[8].angle = 45
kit.servo[12].angle = 45
kit.continuous_servo[4].throttle = 1
time.sleep(1)

kit.continuous_servo[4].throttle = -1
time.sleep(1)

kit.servo[0].angle = 0
kit.servo[8].angle = 0
kit.servo[12].angle = 0
kit.continuous_servo[4].throttle = -1
kit.continuous_servo[4].throttle = 0
