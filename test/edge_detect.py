import cv2 as cv
import numpy as np

def main():
    img = cv.imread('../img/lena.jpg')
    img_edge = cv.Canny(img, 100, 200)
    print(img_edge)
    print(img_edge.shape)
    print(np.min(img_edge))
    print(np.max(img_edge))
    print(np.mean(img_edge))
    print(np.sum(img_edge))
    cv.imshow('edge', img_edge)
    cv.waitKey(0)

if __name__ == '__main__':
    print('- Edge detect -')
    main()