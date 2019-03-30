import RPi.GPIO as GPIO
import sys
import time

class LED():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def shine(self, count= 2, interval= 0.5):
        for _ in range(count):
            self.turn_on()
            time.sleep(interval)
            self.turn_off()
            time.sleep(interval)

    def __del__(self):
        GPIO.output(self.pin, GPIO.LOW)

if __name__ == '__main__':
    print('- LED -')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pin = int(sys.argv[1])
    led = LED(pin)
    led.shine(2, 0.5)