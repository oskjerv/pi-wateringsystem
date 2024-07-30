import RPi.GPIO
import time
import os
import datetime
import requests

# hardware configuration

pins = [20, 21, 26]

# behavior configuration
open_time = 3 # open the latch for ... seconds

# begin setup code
def PiPinSetup(initial=False):
    RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
    for pin in pins:
        RPi.GPIO.setup(pin, RPi.GPIO.OUT)
        if initial:
            RPi.GPIO.output(pin, True)
            RPi.GPIO.output(pin, False)
            
def open_location(pin):
    pin_GPIO = pin
    RPi.GPIO.output(pin_GPIO, False)
    time.sleep(open_time)
    RPi.GPIO.output(pin_GPIO, True)

PiPinSetup()

for k in range(1): # cycle 2 times
   for channel in pins:
       open_location(channel)
       time.sleep(0.5)

RPi.GPIO.cleanup()