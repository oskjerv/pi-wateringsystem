import RPi.GPIO
import time
import os
import datetime
import requests

pin = 21

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(pin, RPi.GPIO.OUT)
#RPi.GPIO.output(pin, True)
RPi.GPIO.output(pin, False)

time.sleep(2)

RPi.GPIO.cleanup()