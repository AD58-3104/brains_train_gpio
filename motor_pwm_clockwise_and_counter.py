#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor_pin_right = 13 #12
motor_right_in1 = 17 #23
motor_right_in2 = 27 #24
GPIO.setup(motor_pin_right, GPIO.OUT)
GPIO.setup(motor_right_in1, GPIO.OUT)
GPIO.setup(motor_right_in2, GPIO.OUT)

motor_pin_left = 12
motor_left_in1 = 23
motor_left_in2 = 24
GPIO.setup(motor_pin_left, GPIO.OUT)
GPIO.setup(motor_left_in1, GPIO.OUT)
GPIO.setup(motor_left_in2, GPIO.OUT)

servo_left = GPIO.PWM(motor_pin_left, 50)
servo_right = GPIO.PWM(motor_pin_right, 50)
servo_right.start(0)
servo_left.start(0)

for i in range(3):
    GPIO.output(motor_right_in1, GPIO.HIGH)
    GPIO.output(motor_right_in2, GPIO.LOW)
    servo_right.ChangeDutyCycle(30)
    GPIO.output(motor_left_in1, GPIO.HIGH)
    GPIO.output(motor_left_in2, GPIO.LOW)
    servo_left.ChangeDutyCycle(30)
    time.sleep(1)

    GPIO.output(motor_right_in1, GPIO.LOW)
    GPIO.output(motor_right_in2, GPIO.HIGH)
    servo_right.ChangeDutyCycle(30)
    GPIO.output(motor_left_in1, GPIO.LOW)
    GPIO.output(motor_left_in2, GPIO.HIGH)
    servo_left.ChangeDutyCycle(30)
    time.sleep(1)

servo_right.stop()
servo_left.stop()
GPIO.cleanup()