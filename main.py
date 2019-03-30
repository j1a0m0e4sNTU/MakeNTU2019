import RPi.GPIO as GPIO
from transfer import *
from picamera import PiCamera
from motor import Motor
from face_detection import Face_detector
from LED import LED
from button import Button
from normal import *
from upload import upload
import cv2 as cv
import numpy as np
import time
import datetime


class Shit_detector():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.state_list = ['IDLE']
        self.cur_state = self.state_list[0]
        self.green_led = LED(5)
        self.yellow_led = LED(13)
        self.red_led = LED(21)
        self.motor = Motor()
        self.web_cam = cv.VideoCapture(0)
        self.pi_cam = PiCamera()

        self.angle = 0.25
        self.open = False
        self.face = None

        self.server_ip = '10.10.3.21'
        self.port = 8080
        
        self.threshold = 20000000

    def lock(self):
        self.motor.rotate(self.angle)

    def unlock(self):
        self.motor.rotate(-1 * self.angle)

    def reset(self):
        self.pi_cam.capture('origin.jpg')
        self.lock()
        self.cur_state = 'IDLE'

    def detect_face(self):
        def call_back(channel):
            self.open = True

        button = Button(4, call_back)
        detector = Face_detector()
        
        while True:
            _, img = self.web_cam.read()
            if detector.has_face(img):
                self.green_led.turn_on()
                time.sleep(2)
                detector.mark_face(img)
                if self.open:
                    self.face = img
                    break
            else:
                self.green_led.turn_off()

        self.green_led.turn_off()

    def wait_for_flush(self):
        client_socket = socket.socket(socket.AF_INET)
        client_socket.connect((self.server_ip, self.port))
        client_socket.recv(1024)
        client_socket.close()
        print('flushed !')

    def detect_shit(self, img_after):
        img_origin = cv.imread('origin.jpg')
        similarity = get_similarity(img_origin, img_after, normal)
        if similarity > self.threshold:
            file_name = datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '_')
            cv.imwrite('face.jpg', self.face)
            upload('.','face.jpg', file_name +'_face.jpg')
            cv.imwrite('shit.jpg', img_after)
            upload('.','shit.jpg', file_name +'_shit.jpg')

    def run(self):
        pass

    def test(self):
        print('start detect')
        self.detect_face()
        cv.imwrite('face.jpg', self.face) 
        print('finish')
    
    def test2(self):
        self.reset()
        print('finish saving origin.jpg')
        self.detect_face()
        print('finish detect face')
        _, img = self.pi_cam.read()
        self.detect_shit(img)
        print('finish detect shit')

if __name__ == '__main__':
    print('- MAIN -')
    detector = Shit_detector()
    detector.test2()