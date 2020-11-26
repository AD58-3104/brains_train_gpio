import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 4
GPIO.setup(led_pin, GPIO.OUT)

#GPIO.setwarnings(False) 

led1 = GPIO.PWM(led_pin, 50) #50Hz
led1.start(0)

for loop in range(10):
    for i in range(0,60,20):
        led1.ChangeDutyCycle(i)
        time.sleep(0.05)

    for i in range(60,0,-20):
        led1.ChangeDutyCycle(i)
        time.sleep(0.05)
        
led1.stop()
GPIO.cleanup()