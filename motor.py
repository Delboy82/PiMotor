#!/usr/bin/python

#Import modules requied
import RPi.GPIO as GPIO
from time import sleep

#set GPIO mode and disable gpio warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 23
Motor1B = 24
Motor1E = 25


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


print "Turning Motor On"

GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(10)
GPIO.output(Motor1E,GPIO.LOW)
sleep(10)

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(10)

print "Stopping Motor"

GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()


