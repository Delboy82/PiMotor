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
timer = 10

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


def MotorUp():
   print "Turning Motor On Up in 10 seconds"
   sleep(10)
   GPIO.output(Motor1A,GPIO.LOW)
   GPIO.output(Motor1B,GPIO.HIGH)
   GPIO.output(Motor1E,GPIO.HIGH)
   sleep(timer)
   GPIO.output(Motor1E,GPIO.LOW)

def Motordown():
   print "Turning Motor On Down"
   GPIO.output(Motor1A,GPIO.HIGH)
   GPIO.output(Motor1B,GPIO.LOW)
   GPIO.output(Motor1E,GPIO.HIGH)
   sleep(timer)
   GPIO.output(Motor1E,GPIO.LOW)

##print "Stopping Motor"


#Motordown()
#sleep(timer)
MotorUp()
GPIO.output(Motor1E,GPIO.LOW)
GPIO.cleanup()


