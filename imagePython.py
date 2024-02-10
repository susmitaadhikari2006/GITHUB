import cv2
import numpy

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_orange = numpy.array([0, 102, 204])
    upper_orange = numpy.array([20, 255, 255])
        
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # frame = cv2.flip(-1)
    
    cv2.imshow('FRC Image Processing', result)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()