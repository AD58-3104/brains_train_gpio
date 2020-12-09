#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensor_right = 7
sensor_left = 6
motor_right = 13
motor_left = 14
GPIO.setup(motor_right, GPIO.OUT)
GPIO.setup(motor_left, GPIO.OUT)
GPIO.setup(sensor_left, GPIO.IN)
GPIO.setup(sensor_right, GPIO.IN)


servo_left = GPIO.PWM(motor_left, 50)
servo_right = GPIO.PWM(motor_right, 50)

servo_left.start(0)
servo_right.start(0)



while True:
    if GPIO.input(sensor_right) == True:
        print("right is true")
    else if GPIO.input(sensor_left) == True:
        print("left is true")

servo_right.stop()
servo_left.stop()
GPIO.cleanup()