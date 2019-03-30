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

def normal2(name):
    img = cv.imread(name)
    for i in range(3):
        img[:, :, i] = img[:, :, i] - np.mean(img[:, :, i])
    return img

def normal3(name):
    img = cv.imread(name, 0)
    gray_lap = cv.Laplacian(img, cv.CV_16S, ksize= 3)
    dst = cv.convertScaleAbs(gray_lap)
    return dst

def canny_sum(img):
    img_edge = cv.Canny(img, 100, 200)
    edge_sum = np.sum(img_edge)
    return int(edge_sum)

def get_canny_sum_diff(img_0, img_1):
    sum_0 = canny_sum(img_0)
    sum_1 = canny_sum(img_1)
    return abs(sum_0 - sum_1)

if __name__ == '__main__':
    if args.mode == 'shot':
        cam = PiCamera()
        #cam.exposure_mode = 'off'
        #cam.framerate =1
        #cam.shutter_speed = 6000000
        #cam.iso = 1600
        name = args.name + '.jpg'
        cam.capture(name)
        print('saved', name)
    else:
        # img_0 = normal('0.jpg')
        # img_1 = normal('1.jpg')

        # dis = np.absolute(img_0 - img_1)
        # diff = np.sum(dis)
        # s = int(diff)
        # print('diff:', s)
        img_0 = cv.imread('0.jpg')
        img_1 = cv.imread('1.jpg')
        diff = get_canny_sum_diff(img_0, img_1)
        print('Diff:', diff)