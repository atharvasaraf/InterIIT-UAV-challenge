#!/usr/bin/ python 2.7.12
import cv2
import math
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#----------USING WEBCAM----------
#cap = cv2.VideoCapture(0)
#--------------------------------

#----------USING RPICAM----------
camera=PiCamera()
camera.resolution=(320,240)
camera.framerate=60
camera.vflip=True
rawCapture =PiRGBArray(camera)
time.sleep(0.1)
#--------------------------------
print "press ESCAPE to exit"
lower_colour=np.array([20,45,80])
upper_colour=np.array([40,130,220])
minLineLength=0.1
maxLineGap=10

for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
#while True:
	#ret, screen = cap.read()
	screen = frame.array
	hsv=cv2.cvtColor(screen,cv2.COLOR_BGR2HSV)
	blur=cv2.GaussianBlur(hsv,(15,15), 0)
	mask=cv2.inRange(hsv,lower_colour,upper_colour)
	#gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(mask, 50, 150, apertureSize=3)	
	lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 4, minLineLength, maxLineGap)
	if lines is not None:
		for i in range(len(lines)):
			for x1,y1,x2,y2 in lines[i]:
				cv2.line(screen, (x1, y1), (x2, y2), (0, 255, 0), 2)
	cv2.namedWindow('img',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('img',1368,786)
	cv2.imshow('img', screen)
	
	k = cv2.waitKey(1)
	if k == 27:
		break
	else:
		pass
	rawCapture.truncate(0)
#cap.release()
cv2.destroyAllWindows()
