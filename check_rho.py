import cv2
import numpy as np
cap=cv2.VideoCapture(0)
r=0
theta=45/57.71
while True:
	ret, frame = cap.read()
	a=np.cos(theta)
	b=np.sin(theta)
	x0=a*r
	y0=b*r
	x1=int(x0+1000*(-b))
	y1=int(y0+1000*(a))
	x2=int(x0+1000*(-b)) 
	y2=int(y0+1000*(a))
	cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
	k=cv2.waitKey(1)
	if k==27:
		break
	else :
		r=r+20
		cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()

