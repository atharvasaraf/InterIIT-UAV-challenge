#!/usr/bin/ python 2.7.12
import cv2
import numpy as np
import time
import math

# -------------USING WEBCAM---------------------
cap = cv2.VideoCapture(1)
# ----------------------------------------------

# ------------USING RPICAM----------------------
# ----------------------------------------------

# -----Masking parameters for filtering Yellow Colour---
lower_color = np.array([20, 45, 80])
upper_color = np.array([40, 130, 220])
# -----------------------------------------------------_

def getPoint(r1,theta1,r2,theta2):
	ct1=math.cos(theta1)
	st1=math.sin(theta1)
	ct2=math.cos(theta2)
	st2=math.sin(theta2)
	d=ct1*st1-st1*ct2
	if d != 0.0:
		x=int((st2*r1 - st1*r2)/d)
		y=int((-ct2*r1 + ct1*r2)/d)
		return (x,y)
	else:
		return None
prev_theta=0
theta=0
sum_theta=0
prev_r=0
r=0
sum_r=0
while 1:
	sum_r = 0
	sum_theta = 0
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	blur = cv2.GaussianBlur(hsv, (15, 15), 0)
	mask = cv2.inRange(hsv, lower_color, upper_color)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(mask, 35, 230, apertureSize=3)
	lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
	if lines is not None:
		if len(lines)<=4:
			check=len(lines)
		elif len(lines)>4:
			check=4
		for i in range(check):
			for r, theta in lines[i]:
				a = np.cos(theta)
				b = np.sin(theta)
				x0 = a * r
				y0 = b * r
				x1 = int(x0 + 1000 * (-b))
				y1 = int(y0 + 1000 * (a))
				x2 = int(x0 - 1000 * (-b))
				y2 = int(y0 - 1000 * (a))
				cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
				#if theta > -1.57079 and theta <= -0.78539:
				#	theta = 2.35619 + theta
				#elif theta > -0.78539 and theta < 0:
				#	theta = theta + 1.57079
				#if theta >2.35619 and theta<3.14159:
				#	theta=theta-3.14159
				#elif theta>1.57079 and theta<=2.35619:
				#	theta=theta-3.14159
							
				print abs(math.degrees(prev_theta-theta))
				if abs( math.degrees(theta-prev_theta))>=45:
					#print getPoint(r,theta,prev_r,prev_theta), "		",abs(math.degrees(theta-prev_theta))
					cv2.circle(frame,	getPoint(r,theta,prev_r,prev_theta),	10,	(255,0,0),	-1)
				prev_theta=theta
				prev_r=r
			if theta>=2.83 or theta<0.31:
				sum_theta=theta
			else:
				sum_theta = sum_theta + theta
			sum_r = sum_r + (r)
	
		sum_theta = abs(sum_theta / check)
		sum_r = sum_r / check
		a = np.cos(sum_theta)
		b = np.sin(sum_theta)
		x0 = a * sum_r
		y0 = b * sum_r
		x1 = int(x0 + 1000 * (-b))
		y1 = int(y0 + 1000 * (a))
		x2 = int(x0 - 1000 * (-b))
		y2 = int(y0 - 1000 * (a))
		cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
		sum_r = 0
		sum_theta = 0
	
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	cv2.imshow('img',frame)

cap.release()
cv2.destroyAllWindows()
