#!/usr/bin/ python 2.7.12
import cv2
import numpy as np

#-------------USING WEBCAM----------------------
cap = cv2.VideoCapture(0)
#-----------------------------------------------


#------------USING RPICAM----------------------


#-----------------------------------------------



#-----masking parameters for filtering Yellow Colour-------
lower_color = np.array([20, 45, 80])
upper_color = np.array([40, 130, 220])
#-----------------------------------------------------





while 1:
	sum_r=0
	sum_theta=0
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	blur = cv2.GaussianBlur(hsv, (15, 15), 0)
	mask = cv2.inRange(hsv, lower_color, upper_color)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# ----------------------------
	# sobel experimental:
	# gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F,dx=1,dy=0,ksize=-1)
	# gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F,dx=0,dy=1,ksize=-1)
	# gradient=cv2.subtract(gradX,gradY)
	# edges=cv2.convertScaleAbs(gradient)
	# ----------------------------
	# ----------------------------
	# canny is original
	edges = cv2.Canny(mask, 35, 230, apertureSize=3)
	# ----------------------------

	lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
	if lines is not None:
		#sum_r=0
		#sum_theta=0
		for i in range(len(lines)):
			for r, theta in lines[i]:
				if theta>1.57079:
					theta=3.14159-theta
				sum_theta=sum_theta + theta
				sum_r=sum_r+r

				a = np.cos(theta)
				b = np.sin(theta)
				x0 = a * r
				y0 = b * r
				x1 = int(x0 + 1000 * (-b))
				y1 = int(y0 + 1000 * (a))
				x2 = int(x0 - 1000 * (-b))
				y2 = int(y0 - 1000 * (a))
				cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
				#print "r : ",r,"theta : ",theta       			
				#cv2.imwrite('hough_lines.jpg',img)
			sum_theta=sum_theta/len(lines[i])
			sum_r=sum_r/len(lines[i])
			print "sumtheta: ",sum_theta," sumr: ",sum_r, " len: ",len(lines[i]), "	theta",theta,"	r ",r
			a=np.cos(sum_theta)
			b=np.sin(sum_theta)
			x0=a*sum_r
			y0=b*sum_r
			x1=int(x0 + 1000 * (-b))
			y1=int(y0 + 1000 * (a))
			x2=	int(x0 - 1000 * (-b))
			y2=int(y0 - 1000 * (a))
			cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),5)
	sum_r=0
	sum_theta=0
	cv2.imshow('img', frame)
	
	#print(sum_theta*57.281)
	#print(sum_r)
	#cv2.imshow('edges', edges)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
