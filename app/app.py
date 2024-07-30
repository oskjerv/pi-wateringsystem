from flask import Flask, render_template
import RPi.GPIO as GPIO

import datetime
import time

# own modules
import writetodb
import waterpump_scheduler

app = Flask(__name__)

ch1 = 26
ch2 = 20
ch3 = 21



@app.route("/")
def hello():
    now = datetime.datetime.now()
    timestring = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'Montana vannverk',
        'time' : timestring
        }
    return render_template('main.html', **templateData)

@app.route("/<pin>/<action>/<sec>")
def action(pin, action, sec):
    #def waterpump_switch(pin, action, sec):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(int(pin), GPIO.OUT)
    
    if action == "on":
        print('it works')
        # Complete/close the relay circuit
        GPIO.output(int(pin), False)
        # Write event to database
        writetodb.write_watering(int(pin), sec)
        time.sleep(int(sec))
        # Discontinue/open the relay circuit
        GPIO.output(int(pin), True)
        GPIO.cleanup()
    else :
        print('doesnt work')
        GPIO.output(int(pin), True)
        GPIO.cleanup()
    
    now = datetime.datetime.now()
    timestring = now.strftime("%Y-%m-%d %H:%M")
    
    templateData = {
        'title': 'Montana vannverk',
        'time' : timestring,
        'duration': sec, 
        'action_description': 'Vannpumpe pa inngang ' + str(pin) + ' ble skrudd pa i ' + str(sec) + ' sekunder' 
        }
    
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80, debug = True)