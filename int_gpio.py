#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os


# handle the button event
def buttonEventHandler (pin):
    print "handling button event"

    os.system('/home/pi/toggle_4_5.sh >> /dev/null 2>&1')



# main function
def main():

    # tell the GPIO module that we want to use 
    # the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # setup pin 25 as an input
    GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(14,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)

    GPIO.output(14,False)
    GPIO.output(15,True)

    # tell the GPIO library to look out for an 
    # event on pin 25 and deal with it by calling 
    # the buttonEventHandler function
    GPIO.add_event_detect(25,GPIO.FALLING,callback=buttonEventHandler,bouncetime=100)

    while True:
	time.sleep(3600)

    GPIO.cleanup()


if __name__=="__main__":
    main()
