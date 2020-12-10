import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)                         

sensor_right = 22
sensor_left = 9
GPIO.setup(sensor_left,GPIO.IN)                                                       
GPIO.setup(sensor_right,GPIO.IN)                                                       


def switch_callback(gpio_pin):
    print(gpio_pin)
    print("falling")



GPIO.add_event_detect(sensor_left, GPIO.FALLING,bouncetime=50)
GPIO.add_event_detect(sensor_right, GPIO.FALLING,bouncetime=50)

GPIO.add_event_callback(sensor_left, switch_callback)     
GPIO.add_event_callback(sensor_right, switch_callback)   

try:
    while True:
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()