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
    edges = cv2.Canny(mask, 20, 250, apertureSize=3)

    # ----------------------------
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
    if lines is not None:
        for i in range(len(lines)):
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
            # cv2.imwrite('hough_lines.jpg',img)
    cv2.imshow('img', frame)
    cv2.imshow('edges', edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()