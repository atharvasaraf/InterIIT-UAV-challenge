#!/usr/bin/ python 2.7.12
#have to put correction for secondary line detection

import cv2
import numpy as np
import time
import math
import time

#---------------USING WEBCAM------------------------------------
cap = cv2.VideoCapture(0)
# --------------------------------------------------------------

#----------------HSV FOR YELLOW COLOUR--------------------------
lower_color = np.array([20, 45, 80])
upper_color = np.array([40, 130, 220])
# --------------------------------------------------------------


#----------------DEFINING SOME FUNCTIONS------------------------


#---------------findPoints function-----------------------------
#----Returns (x1,y1)and(x2,y2) of line for given (r,theta)------
def findPoints(r,theta,length):
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * r
	y0 = b * r
	x1 = int(x0 + length * (-b))
	y1 = int(y0 + length * (a))
	x2 = int(x0 - length * (-b))
	y2 = int(y0 - length * (a))
	return [(x1,y1),(x2,y2)]
#---------------------------------------------------------------	


while 1:
	#setting all working variables to default after every loop-----
	sum_theta_secondary=0
	sum_theta_main=0
	sum_r_main=0
	sum_r_secondary=0
	count_secondary=0
	count_main=0
	a=[]
	
	#capture a frame from the video feed
	ret, frame = cap.read()
	if ret==False:
		continue
	#---------------Resize Image to Half------------------------
	frame=cv2.resize(frame,(0,0),fx=0.35,fy=0.35)
	#---------------Applying Transforms and Filters--------------
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#blur = cv2.GaussianBlur(hsv, (15, 15), 0)
	mask = cv2.inRange(hsv, lower_color, upper_color)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(mask, 35, 230, apertureSize=3)
	
	#---------------Line Detection Using HoughLines function-------
	lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
	
	
	#---------------Execute while lines are found------------------
	if lines is not None:
		
		#-------------Picking a Maximum of 4 longest lines---------
		if len(lines)<=20:
			check=len(lines)
		elif len(lines)>20:
			check=20
		
		#--------------Looping through each line ------------------------
		for i in range(check):
			for r, theta in lines[i]:			
				#making an array of the r found for boundary conditions-----
				a=np.append(a,r)
				
				#--Call findPoints function to obtain cartesian of line--
				points=findPoints(r,theta,1000)
				
				#-----Transform found lines appropriately for averaging----- 
				if r < 0:
					theta=theta-math.radians(180)	
				
				#-----Identify angle difference between current line and Vertical--
				theta_diff=np.degrees(theta)
				
				#------Classify line as Primary or Secondary based on the Angle perceived
				if theta_diff>45 and theta_diff<135:
					sum_theta_secondary=sum_theta_secondary+theta
					sum_r_secondary=sum_r_secondary+abs(r)
					count_secondary=count_secondary+1
				else :
					sum_theta_main=sum_theta_main+theta
					sum_r_main=sum_r_main+abs(r)
					count_main=count_main+1

			    	
				#----------------Draw found line in Green---------------
				cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
												
				#-----------Compute Sum for averaging -----------
		a=np.sign(a)
		if count_main is not 0:
			sum_theta_main = sum_theta_main / count_main
			sum_r_main = sum_r_main / count_main
		if count_secondary is not 0:
			sum_theta_secondary=sum_theta_secondary/count_secondary
			sum_r_secondary=sum_r_secondary/count_secondary
	 	
		#-------Correction for boundary conditions--------------
		if abs(np.sum(a))>=len(a):
			points=findPoints(sum_r_main,sum_theta_main,1000)
		else :
			points=findPoints(lines[0][0][0],lines[0][0][1],1000)
		
		#-------Draw Primary and Secondary lines after averaging and applying boundary condition
		cv2.line(frame,points[0],points[1],(0,0,255),2)
		points=findPoints(sum_r_secondary,sum_theta_secondary,30)
		cv2.line(frame,points[0],points[1],(255,0,0),2)
	
	#--------------Check User Command for Loop termination------
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	#---------------Show Image where lines have been identified-------------------------------------
	cv2.namedWindow('img',cv2.CV_WINDOW_AUTOSIZE)
	cv2.resizeWindow('img',768,640)
	#frame=cv2.resize(frame,(0,0),fx=8,fy=8)
	#print frame.shape
	
	#print np.degrees(sum_theta_secondary),"			Pos Y",	
	
	sin_theta=(np.sin(sum_theta_secondary))
	
	#pos_y_secondary= sum_r_secondary*sin_theta + 84*np.tan(sum_theta_secondary)- sum_r_secondary*sin_theta
	pos_y_secondary=sum_r_secondary*sin_theta
	pos_y_secondary=int(pos_y_secondary)
	#print pos_y_secondary
	if sum_r_main !=0 and sum_theta_main !=0:
		x_primary=(112-(sum_r_main*np.sin(sum_theta_main)))
		x_primary=x_primary/np.tan(sum_theta_main)
		x_primary+=sum_r_main*np.cos(sum_theta_main)
		x_primary=int(x_primary)
		#cv2.circle(frame,(x_primary,112),9,(0,255,0),-1)

		cv2.imshow('img',frame)
	
cap.release()

cv2.destroyAllWindows()
