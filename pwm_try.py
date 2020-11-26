import sys
import time
from wiringpi import *


if __name__ == '__main__':
    wiringPiSetupGpio()
    pinMode(24,GPIO.PWM_OUTPUT)
    digitalWrite(24,1)
    time.sleep(5)
    digitalWrite(24,0)
