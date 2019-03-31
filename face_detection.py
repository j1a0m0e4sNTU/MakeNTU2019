import cv2 as cv
import numpy as np
from LED import LED

class Face_detector():
    def __init__(self, path= './filters/haarcascade_frontalface_default.xml', scaleFactor= 2, minNeighobrs= 3):
        self.detector = cv.CascadeClassifier(path)
        self.scaleFactor = scaleFactor
        self.minNeighobrs = minNeighobrs

    def mark_face(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(img_gray, scaleFactor= self.scaleFactor, minNeighbors= self.minNeighobrs)
       
        for (x,y,w,h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    def has_face(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(img_gray, scaleFactor= self.scaleFactor, minNeighbors= self.minNeighobrs)
        
        if (len(faces) > 0):
            return True
        else:
            return False


if __name__ == '__main__':
    import argparse
    parser.add_argument('-s', type= int, default= 2)
    parser.add_argument('-m', type= int, default= 3)
    args = parser.parse_args()

    cam = cv.VideoCapture(0)
    face_detector = Face_detector(args.s, args.m)
    green_led = LED(5)
    while True:
        _, img = cam.read()
        # face_detector.mark_face(img)
        # cv.imshow('Face detection', img)
        if detector.has_face(img):
            green_led.turn_on()
        else:
            green_led.turn_off()

        if cv.waitKey(1) == ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()