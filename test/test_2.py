import cv2 as cv 
from imutils.video import VideoStream

vs = VideoStream(src=0).start()

while True:
    frame = vs.read()
    cv.imshow('video', frame)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
vs.stop()