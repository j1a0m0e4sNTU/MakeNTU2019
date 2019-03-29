import cv2 as cv 

cam = cv.VideoCapture(0)


while True:
    _, img = cam.read()
    cv.imshow('video',img)
    if cv.waitKey(1)  == ord('q'):
        break
     
cam.release()
cv.destroyAllWindows()
