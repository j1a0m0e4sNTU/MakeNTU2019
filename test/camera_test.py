import cv2 as cv 
# from imutils.video import VideoStream


def test1():
    vs = VideoStream(src=0).start()

    while True:
        frame = vs.read()
        cv.imshow('video', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cv.destroyAllWindows()
    vs.stop()

def test2():
    cam = cv.VideoCapture(0)

    while True:
        _, img = cam.read()
        cv.imshow('video',img)
        if cv.waitKey(1)  == ord('q'):
            break
     
    cam.release()
    cv.destroyAllWindows()

def test3():
    cam = cv.VideoCapture(0)
    _, img = cam.read()
    cv.imwrite('web.jpg', img)

if __name__ == '__main__':
    print('test')
    test3()
