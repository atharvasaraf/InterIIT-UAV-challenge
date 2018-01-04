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
	if length==30:
		x1=107
		x2=137
	return [(x1,y1),(x2,y2)]
#---------------------------------------------------------------	

#---------------------------------------------------------------
marker_count=0
flag=0
while 1:
	#setting all working variables to default after every loop-----
	sum_theta_secondary=0
	sum_theta_main=0
	sum_r_main=0
	sum_r_secondary=0
	count_secondary=0
	count_main=0
	k=-1
	a=[]
	
	#capture a frame from the video feed
	ret, frame = cap.read()
	if ret==False:
		continue
	
	#---------------Resize Image to Half------------------------
	frame=cv2.resize(frame,(0,0),fx=0.35,fy=0.35)
	#---------------Applying Transforms and Filters--------------
	#frame=frame[21:147]
	#print frame.shape
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
				
				if k==-1 and abs(theta_diff)<=45:
					k=i
				#------Classify line as Primary or Secondary based on the Angle perceived
				if theta_diff>45 and theta_diff<135:
					if flag ==1 and abs(r)<= 63:
						flag=0
					if flag==0:
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
		elif k is not -1 :
			points=findPoints(lines[k][0][0],lines[k][0][1],1000)
		
		#-------Draw Primary and Secondary lines after averaging and applying boundary condition
		cv2.line(frame,points[0],points[1],(0,0,255),2)
		points=findPoints(sum_r_secondary,sum_theta_secondary,30)
		#cv2.line(frame,points[0],points[1],(255,0,0),2)
	
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
	
	if abs(np.tan(sum_theta_secondary))<0.01:
		pos_y_secondary=112
	else:
		pos_y_secondary= sum_r_secondary*sin_theta + 112/np.tan(sum_theta_secondary)- sum_r_secondary*sin_theta
		pos_y_secondary=sum_r_secondary*sin_theta
		pos_y_secondary=int(pos_y_secondary)
	#print pos_y_secondary
	if count_secondary and pos_y_secondary<126 and pos_y_secondary>0:
		cv2.circle(frame,(112,pos_y_secondary),5,(255,255,255),-1)
		if pos_y_secondary>80:
			flag=1
			print "crossed a marker",
			marker_count+=1	
			print marker_count
	if sum_r_main !=0 and sum_theta_main !=0 :
		tan_theta=np.tan(sum_theta_main)
		x_primary=(63-(sum_r_main*np.sin(sum_theta_main)))
		x_primary=x_primary*np.tan(sum_theta_main)
		x_primary+=sum_r_main*np.cos(sum_theta_main)
		x_primary=int(x_primary)
		#print x_primary
		cv2.line(frame,(x_primary,63),(112,63),(0,0,0),2)
		cv2.circle(frame,(x_primary,63),5,(0,0,0),-1)
	else:
			pass
	cv2.imshow('img',frame)
	
cap.release()

cv2.destroyAllWindows()
