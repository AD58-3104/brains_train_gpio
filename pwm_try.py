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
    wiringPiSetupGpio()
    pinMode(24,GPIO.PWM_OUTPUT)
    digitalWrite(24,1)
    time.sleep(5)
    digitalWrite(24,0)
