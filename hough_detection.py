#!/usr/bin/ python 2.7.12
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	edges=cv2.Canny(gray,50,150,apertureSize=3)
	lines=cv2.HoughLines(edges,1,np.pi/180,200)
	if lines[0].all != None :		
		for r,theta in lines[0]:
			a=np.cos(theta)
			b=np.sin(theta)
			x0=a*r
			y0=b*r
			x1=int(x0+1000*(-b))
			y1=int(y0+1000*(a))
			x2=int(x0-1000*(-b))
			y2=int(y0-1000*(a))
			cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
		#cv2.imwrite('hough_lines.jpg',img)
		cv2.imshow('img',frame)
	
	k= cv2.waitKey(5) & 0xFF
	if (k==27): break
cap.release()
cv2.destroyAllWindows()
