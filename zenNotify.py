from zenpy import Zenpy
import RPI.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)

credentials = {
    'email': 'your email',
    'password': 'your password',
    'subdomain': 'your subdomain'
}
zenpy_client = Zenpy(**credentials)

# turn RGB LED off
def turnoff():
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)


def low():
    GPIO.output(blue, 1) # set rgb to blue


def normal():
    GPIO.output(green, 1) # set rgb to green


def high():
    GPIO.output(blue, 1) # set rgb to yellow
    GPIO.output(green, 1)

def urgent():
    GPIO.output(red, 1) # set rgb to red


# RGB LED pin mapping.
red = {{ 8 }}
green = {{ 10 }}
blue = {{ 12 }}

# Set RGB LED pins as output
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

turnoff() #init rgb as off for start

last_hour = datetime.datetime.now() - datetime.timedelta(hours=1)
current_hour = datetime.datetime.now()
for ticket in zenpy_client.search("zenpy", created_between=[last_hour, current_hour], type='ticket', minus='negated'):
    tp = ticket.priority

    if tp == 'Low':
        low() # turn rgb blue
        time.sleep(2000) # wait for 2 seconds
        turnoff() # turn off the RGB
    if tp == 'Normal':
        normal() # turn rgb green
        time.sleep(2000) # wait for 2 seconds
        turnoff() # turn off the RGB
    if tp == 'High':
        high() # turn rgb yellow
        time.sleep(2000) # wait for 2 seconds
        turnoff() # turn off the RGB
    if tp == 'Urgent':
        for i in range(2): # blink rgb 3 times
            urgent() # turn rgb red
            time.sleep(500) # wait for 2 seconds
            turnoff() # turn off the RGB

