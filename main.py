import RPi.GPIO as GPIO
from transfer import *
# from picamera import PiCamera
from motor import Motor
from face_detection import Face_detector

class Shit_detector():
    def __init__(self):
        self.name = 'Shit'
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    

if __name__ == '__main__':
    print('- MAIN -')