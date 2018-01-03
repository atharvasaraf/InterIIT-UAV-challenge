#!/usr/bin/ python 2.7.12
import cv2
import numpy as np
import time
import math
import time

#---------------USING WEBCAM------------------------------------
cap = cv2.VideoCapture(0)
# --------------------------------------------------------------


#----------------USING RPICAM-----------------------------------
# --------------------------------------------------------------


#----------------HSV FOR YELLOW COLOUR--------------------------
lower_color = np.array([20, 45, 80])
upper_color = np.array([40, 130, 220])
# --------------------------------------------------------------


#----------------DEFINING SOME FUNCTIONS------------------------


#---------------findPoints function-----------------------------
#----Returns (x1,y1)and(x2,y2) of line for given (r,theta)------
def findPoints(r,theta):
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * r
	y0 = b * r
	x1 = int(x0 + 1000 * (-b))
	y1 = int(y0 + 1000 * (a))
	x2 = int(x0 - 1000 * (-b))
	y2 = int(y0 - 1000 * (a))
	return [(x1,y1),(x2,y2)]
#---------------------------------------------------------------	


#---------------getPoint function-------------------------------
#----Return Intersection of 2 polar lines in cartesian----------
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
#---------------------------------------------------------------


while 1:
	#setting all working variables to default after every loop-----
	sum_theta=0
	sum_r=0
	a=[]
	flag=0
	#capture a frame from the video feed
	ret, frame = cap.read()
	
	#---------------Applying Transforms and Filters--------------
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	blur = cv2.GaussianBlur(hsv, (15, 15), 0)
	mask = cv2.inRange(hsv, lower_color, upper_color)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(mask, 35, 230, apertureSize=3)
	
	#---------------Line Detection Using HoughLines function-------
	lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
	
	#---------------Execute while lines are found------------------
	if lines is not None:
		
		#-------------Picking a Maximum of 4 longest lines---------
		if len(lines)<=4:
			check=len(lines)
		elif len(lines)>4:
			check=4
		
		#--------------Loop through each line ------------------------
		for i in range(check):
			for r, theta in lines[i]:			
				
				#--Call findPoints function to obtain cartesian of line--
				points=findPoints(r,theta)
				
				#-----Identify angle difference between current line and longest line--
				theta_diff=np.degrees(abs(theta-lines[0][0][1]))
				if theta_diff>20 and theta_diff<160:
					print "Detecting some shit.....",theta_diff
					flag=1
				
				#----------------Draw found line in Green---------------
				cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
				
				#----------Adjust angle for -ve r----------------------
				if r < 0:
					theta=theta-math.radians(180)	
				
				#-----------Compute Sum for averaging -----------
				sum_theta=sum_theta+theta
				sum_r=sum_r+abs(r)
			#------------Add
			a=np.append(a,np.degrees(theta))									
		sum_theta = sum_theta / check
		sum_r = sum_r / check
		a=np.sign(a)
		a=np.sum(a)
		#print a
		if abs(a)<4 or flag==1:
			for i in range(check):
				theta=np.degrees(lines[i][0][1])#adding condition for main line here for over lapping --source r theta
				if theta>35 and theta<145:
					pass
				else:
					points=findPoints(lines[i][0][0],lines[i][0][1])
					cv2.line(frame,points[0],points[1],(0,0,255),4)
					print("doing overlap")
					break
		else:
			avg_points=findPoints(sum_r,sum_theta)
			cv2.line(frame, avg_points[0], avg_points[1], (0, 0, 255), 2)
			print("doing averaging")
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	cv2.imshow('img',frame)

cap.release()
cv2.destroyAllWindows()
