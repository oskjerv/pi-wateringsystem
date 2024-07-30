import time
import RPi.GPIO as GPIO
import writetodb

def turn_on_waterpump(pin, sec):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(int(pin), GPIO.OUT)
    
    #print('it works')
    # Complete/close the relay circuit
    GPIO.output(int(pin), False)
    # Write event to database
    writetodb.write_watering(int(pin), sec)
    time.sleep(int(sec))
    # Discontinue/open the relay circuit
    GPIO.output(int(pin), True)
    GPIO.cleanup()
    
turn_on_waterpump(26, 10)

# 10 seconds ~2.25 dl water
# 20 seconds ~4.5 dl water
