#!/usr/b`in/ python 2.7.12
import cv2
import numpy as np

# -------------USING WEBCAM----------------------
cap = cv2.VideoCapture(1)
# -----------------------------------------------

# ------------USING RPICAM----------------------


# -----------------------------------------------

# -----Masking parameters for filtering Yellow Colour-------
lower_color = np.array([20, 45, 80])
upper_color = np.array([40, 130, 220])
# -----------------------------------------------------

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
        lines = lines[:4:]
        for r, theta in lines:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * r
            y0 = b * r
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            if -1.57079 < theta <= -0.78539:
                theta = 2.35619 + theta
            elif -0.78539 < theta < 0:
                theta = theta + 1.57079
        g1 = filter(lambda l: 0.78539 < l[1] <= 2.35619, lines)
        g2 = filter(lambda l : 0<l[1]<=0.78539 or 2.35619 < l[1] <= 1.57079,lines)
        g1_theta_average = np.average([a[1] for a in lines])
		g1_r_average = np.average([a[1] for a in lines])
		g1_theta_average = np.average([a[1] for a in lines])
		g1_theta_average = np.average([a[1] for a in lines])
# for i in range(check):
    #     for r, theta in lines[i]:
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a * r
    #         y0 = b * r
    #         x1 = int(x0 + 1000 * (-b))
    #         y1 = int(y0 + 1000 * (a))
    #         x2 = int(x0 - 1000 * (-b))
    #         y2 = int(y0 - 1000 * (a))
    #         cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #
    #     if theta > -1.57079 and theta <= -0.78539:
    #         theta = 2.35619 + theta
    #     elif theta > -0.78539 and theta < 0:
    #         theta = theta + 1.57079
    #     sum_theta = sum_theta + theta
    #     sum_r = sum_r + r
    #
    # sum_theta = sum_theta / check
    # sum_r = sum_r / check
    # a = np.cos(sum_theta)
    # b = np.sin(sum_theta)
    # x0 = a * sum_r
    # y0 = b * sum_r
    # x1 = int(x0 + 1000 * (-b))
    # y1 = int(y0 + 1000 * (a))
    # x2 = int(x0 - 1000 * (-b))
    # y2 = int(y0 - 1000 * (a))
    # cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

    # sum_r = 0
    # sum_theta = 0
    cv2.imshow('img', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
