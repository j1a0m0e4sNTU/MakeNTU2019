import cv2 as cv
import numpy as np

class Face_detector():
    def __init__(self, path= './filters/haarcascade_frontalface_default.xml', scaleFactor= 2, minNeighobrs= 3):
        self.detector = cv.CascadeClassifier(path)
        self.scaleFactor = scaleFactor
        self.minNeighobrs = minNeighobrs

    def mark_face(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(img_gray, scaleFactor= self.scaleFactor, minNeighbors= self.minNeighobrs)
       
        for (x,y,w,h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

    def has_face(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(img_gray, scaleFactor= self.scaleFactor, minNeighbors= self.minNeighobrs)
        
        if (len(faces) > 0):
            return True
        else:
            return False

if __name__ == '__main__':
    cam = cv.VideoCapture(0)
    face_detector = Face_detector()
    while True:
        _, img = cam.read()
        face_detector.mark_face(img)
        cv.imshow('Face detection', img)
        
        if cv.waitKey(1) == ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()