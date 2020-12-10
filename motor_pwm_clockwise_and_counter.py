#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor_pin = 13 #12
motor_in1 = 17 #23
motor_in2 = 27 #24
GPIO.setup(motor_pin, GPIO.OUT)
GPIO.setup(motor_in1, GPIO.OUT)
GPIO.setup(motor_in2, GPIO.OUT)

servo = GPIO.PWM(motor_pin, 50)
servo.start(0)

for i in range(3):
    GPIO.output(motor_in1, GPIO.HIGH)
    GPIO.output(motor_in2, GPIO.LOW)
    servo.ChangeDutyCycle(30)
    time.sleep(1)

    GPIO.output(motor_in1, GPIO.LOW)
    GPIO.output(motor_in2, GPIO.HIGH)
    servo.ChangeDutyCycle(30)
    time.sleep(1)

servo.stop()
GPIO.cleanup()