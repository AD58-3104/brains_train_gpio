#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor_pin = #指定
GPIO.setup(motor_pin, GPIO.OUT)

servo = GPIO.PWM(motor_pin, 50)
servo.start(0)

for i in range(3):
    servo.ChangeDutyCycle(5)
    time.sleep(1)

    servo.ChangeDutyCycle(30)
    time.sleep(1)

servo.stop()
GPIO.cleanup()