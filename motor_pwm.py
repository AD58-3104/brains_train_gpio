import sys
import time
from wiringpi import *

PWM_PIN = [18,13]

def setupMotor(id):
    wiringPiSetupGpio()
    pinMode(id,GPIO.PWM_OUTPUT)
    pwmSetMode(GPIO.PWM_MODE_MS)
    pwmSetRange(1920)
    pwmSetClock(200)

if __name__ == '__main__':

    try:
        id = PWM_PIN[int(sys.argv[2])]
        angle = (sys.argv[2])

        if angle == 0:
            setupMotor(id)
            pwmWrite(id,0)
        
        elif angle < 44 or angle > 232:
            print("ERROR: over range")
        else:
            setupMotor(id)
            pwmWrite(id,angle)
            time.sleep(0.5)
            pwmWrite(id,0)

    except:
        print("Usage:argv[0] PWM_ID Count")