#!/usr/bin/ python 2.7.12
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
def findPoints(line,length):
	if line is not None:
		if length==1:	
			line_length=40
		else:
			line_length=1000
		a = np.cos((line[1]))
		b = np.sin((line[1]))
		x0 = a * (line[0])
		y0 = b * (line[0])
		x1 = int(x0 + line_length * (-b))
		y1 = int(y0 + line_length * (a))
		x2 = int(x0 - line_length * (-b))
		y2 = int(y0 - line_length * (a))
		return [(x1,y1),(x2,y2)]
#---------------------------------------------------------------	

#-----------------makeLines function----------------------------
#---------draws lines when fed in two points on line------------
def makeLines(frame,line,check):
	if check==0:
		colour=(0,0,255)
	else:
		colour=(255,0,0)
	cv2.line(frame,line[0],line[1],colour,4)
	
	
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

#----------------getAverage function----------------------------
#----------Returns avarage of line array-------------------------
#----------optimize signum function here itself!!!!!!!!
def getAverage(pseud_lines):
	average_r=0
	average_theta=0
	k=0
	print pseud_lines ,"		blah blah blah"
	print len(pseud_lines),"len lines here"
	for k in range(len(pseud_lines)):
		if (pseud_lines[k][0]) < 0:
			psued_lines[k][1] -= math.radians(180)
		average_r = average_r + pseud_lines[k][0]
		average_theta = average_theta + pseud_lines[k][1]
	average_r = average_r / len(pseud_lines)
	average_theta = average_theta / len(pseud_lines)
	return (average_r,average_theta)
#---------------------------------------------------------------


while 1:
	#setting all working variables to default after every loop-----
	sum_main=np.array([[]])
	sum_marker=np.array([[]])
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
		count=0
		#--------------Loop through each line ------------------------
		for i in range(check):
			for r, theta in lines[i]:			
				
				#--Call findPoints function to obtain cartesian of line--
				points=findPoints((lines[i][0][0],lines[i][0][1]),0)	
				#-----Identify angle difference between current line and vertical--
				#theta_diff=np.degrees(abs(theta-lines[0][0][1]))
				theta_diff=np.degrees(theta)
				if theta_diff>45 and theta_diff<135:
					if sum_marker.size == 0:
						sum_marker=np.append(sum_marker,[r,theta])
					else:
						sum_marker=np.append([sum_marker],[[r,theta]],axis=0)
				else:
					if sum_main.size==0:
						sum_main=np.append(sum_main,[r,theta])
					else:
						sum_main=np.append([sum_main],[[r,theta]],axis=0)
					
				#----------------Draw found line in Green---------------
				cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
				
				
				#-----------Compute Sum for averaging -----------
				if len(sum_marker) is not 0:
					print sum_marker,"HERE!!!!"
					avg_marker = getAverage(sum_marker)
					line_marker = findPoints(avg_marker,1)
					makeLines(frame,line_marker,1)
				if len(sum_main) is not 0:
					avg_main = getAverage(sum_main)
					line_main=findPoints(avg_main,0)
					makeLines(frame,line_main,0)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	cv2.imshow('img',frame)

cap.release()
cv2.destroyAllWindows()
