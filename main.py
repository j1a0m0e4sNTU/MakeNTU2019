import RPi.GPIO as GPIO
from transfer import *
from picamera import PiCamera
from motor import Motor
from face_detection import Face_detector
from LED import LED

class Shit_detector():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.green_led = LED(5)
        self.yellow_led = LED(13)
        self.red_led = LED(21)

    def test(self):
        self.green_led.shine()
        self.yellow_led.shine()
        self.red_led.shine()  

if __name__ == '__main__':
    print('- MAIN -')
    detector = Shit_detector()
    detector.test()