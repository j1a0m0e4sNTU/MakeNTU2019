import cv2 as cv
import numpy as np
from picamera import PiCamera
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['shot', 'diff'])
parser.add_argument('-name', choices=['0','1'])
args = parser.parse_args()

def normal(name):
    img = cv.imread(name)
    img_s = img[:, :, 0] + img[:, :, 1] + img[:, :, 2]
    mean = np.mean(img_s)
    img_n = img_s - mean
    return img_n 

if __name__ == '__main__':
    if args.mode == 'shot':
        cam = PiCamera()
        name = args.name + '.jpg'
        cam.capture(name)
        print('saved', name)
    else:
        img_0 = normal('0.jpg')
        img_1 = normal('1.jpg')

        diff = np.sum(img_0 - img_1)
        s = np.sum(diff)
        print('diff:', s)