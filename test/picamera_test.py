from picamera import PiCamera
import time

cam = PiCamera()
def test1():
    cam.start_preview()
    time.sleep(10)
    cam.stop_preview()

def test2():
    cam.capture('test2.jpg')

if __name__ == '__main__':
    test2()
