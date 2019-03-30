import cv2 as cv
import numpy as np
from picamera import PiCamera
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['shot', 'diff'])
parser.add_argument('-name', choices=['0','1'])
args = parser.parse_args()

if __name__ == '__main__':
    if args.mode == 'shot':
        cam = PiCamera()
        name = args.name + '.jpg'
        cam.capture(name)
        print('saved', name)
    else:
        img_0 = cv.imread('0.jpg')
        img_1 = cv.imread('1.jpg')

        diff = cv.absdiff(img_0, img_1)
        s = np.sum(diff)
        print('diff:', s)