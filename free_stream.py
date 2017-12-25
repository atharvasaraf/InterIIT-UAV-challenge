import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#-----------VIDEOSTREAM FOR RPI_CAM---------------
camera=PiCamera()
camera.resolution=(640,480)
camera.framerate=60
camera.vflip=True
rawCapture=PiRGBArray(camera)
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
	screen=frame.array
	cv2.imshow('freestream',screen)
	rawCapture.truncate(0)
	k=cv2.waitKey(1)
	if(k==27):
		break
cv2.destroyAllWindows()

