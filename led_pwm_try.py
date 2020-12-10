#!/usr/bin/python
# ラズパイ上でledを制御する練習
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led_pin_pwm = 12 
led_pin_digital = 17

GPIO.setup(led_pin_digital,OUT)
GPIO.setup(led_pin_pwm,OUT)

led_pwm = GPIO.PWM(led_pin_pwm)

led_pwm.start(0)

for loop in range(10):
    for i in range(0,50,20)
        led_pwm.ChangeDutyCycle(i)
        GPIO.output(led_pin_digital,GPIO.HIGH)
        #何か追加して交互に光らせるようにする
        time.sleep(0.2)
