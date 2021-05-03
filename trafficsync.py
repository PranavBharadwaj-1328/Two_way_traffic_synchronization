import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
red = 8
yellow = 7
green = 12
red1 = 16
yellow1 = 18
green1 = 22
button = 10
GPIO.setup(red,GPIO.OUT,initial=0)
GPIO.setup(yellow,GPIO.OUT,initial=0)
GPIO.setup(green,GPIO.OUT,initial=0)
GPIO.setup(red1,GPIO.OUT,initial=0)
GPIO.setup(yellow1,GPIO.OUT,initial=0)
GPIO.setup(green1,GPIO.OUT,initial=0)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.output(green1,1)
GPIO.output(red,1)
while (True):
    if(GPIO.input(button) == False and (GPIO.input(green1) == True or GPIO.input(yellow1) == True)):
        GPIO.output(green1,0)
        GPIO.output(yellow1,1)
        sleep(1)
        GPIO.output(yellow1,0)
        GPIO.output(red1,1)
        GPIO.output(red,0)
        GPIO.output(yellow,1)
        sleep(1)
        GPIO.output(yellow,0)
        GPIO.output(green,1)

    if(GPIO.input(button) == False and (GPIO.input(green) == True or GPIO.input(yellow) == True)):
        GPIO.output(green,0)
        GPIO.output(yellow,1)
        sleep(1)
        GPIO.output(yellow,0)
        GPIO.output(red,1)
        GPIO.output(red1,0)
        GPIO.output(yellow1,1)
        sleep(1)
        GPIO.output(yellow1,0)
        GPIO.output(green1,1)
