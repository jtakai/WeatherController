from adafruit_servokit import ServoKit

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
