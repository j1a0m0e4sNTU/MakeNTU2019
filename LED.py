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

    def shine(self, count, interval):
        for _ in range(count):
            self.turn_on()
            time.sleep(interval)
            self.turn_off()
            time.sleep(interval)

if __name__ == '__main__':
    print('- LED -')
    pin = int(sys.argv[1])
    led = LED(pin)
    led.shine(10, 0.5)