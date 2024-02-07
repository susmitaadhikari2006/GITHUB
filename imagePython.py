import cv2
import numpy

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    
    cv2.imshow('frame', frame)
    