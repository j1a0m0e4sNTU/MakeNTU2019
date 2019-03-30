import RPi.GPIO as GPIO
import sys
import time

class Button():
    def __init__(self, pin, call_back):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down= GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback= call_back, bouncetime= 300)

if __name__ == '__main__':
    print('- Button -')
    pin = int(sys.argv[1])
    def f():
        print('push')
    button = Button(pin, f)
    while True:
        print('wait ...')
        time.sleep(100)
