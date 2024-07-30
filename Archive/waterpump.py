import RPi.GPIO
import time
import os
import datetime
import requests
import writetodb

# BCM pins relay channels (ch1 = 26, ch2 = 20, ch3 = 21)
pin = 26

def waterpump_switch(pin, sec):
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(pin, RPi.GPIO.OUT)
    
    # Complete/close the relay circuit
    RPi.GPIO.output(pin, False)
    
    # Write event to database
    writetodb.write_watering(pin, sec)
    time.sleep(sec)
    
    # Discontinue/open the relay circuit
    RPi.GPIO.output(pin, True)

waterpump_switch(pin, 10)

RPi.GPIO.cleanup()

