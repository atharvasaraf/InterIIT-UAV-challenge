#!/usr/b`in/ python 2.7.12
import cv2
import numpy as np
import math

# -------------USING WEBCAM----------------------
cap = cv2.VideoCapture(1)
# -----------------------------------------------

# ------------USING RPICAM----------------------


# -----------------------------------------------

# -----Masking parameters for filtering Yellow Colour-------
lower_color = np.array([20, 45, 80])
upper_color = np.array([40, 130, 220])
# -----------------------------------------------------
i = 0
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
        print(lines[0][0][1])
        for line in lines:
            for r, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * r
                y0 = b * r
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * a)
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * a)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        g1_theta_average = np.average([a[0][1] for a in lines])
        g1_r_average = abs(np.average([a[0][0] for a in lines]))
        a = np.cos(g1_theta_average)
        b = np.sin(g1_theta_average)
        x0 = a * g1_r_average
        y0 = b * g1_r_average
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        #         if -1.57079 < theta <= -0.78539:
        #             theta = 2.35619 + theta
        #         elif -0.78539 < theta < 0:
        #             theta = theta + 1.57079
        # g1 = filter(lambda l: math.radians(45) < l[0][1] <= math.radians(135), lines)
        # g2 = filter(lambda l: math.radians(0) < l[0][1] <= math.radians(45) or math.radians(135) < l[i][1] <= math.radians(180), lines)
        # if len(g1) != 0:
        #     g1_theta_average = np.average([a[0][1] for a in g1])
        #     g1_r_average = np.average([a[0][0] for a in g1])
        #     a = np.cos(g1_theta_average)
        #     b = np.sin(g1_theta_average)
        #     x0 = a * g1_r_average
        #     y0 = b * g1_r_average
        #     x1 = int(x0 + 1000 * (-b))
        #     y1 = int(y0 + 1000 * a)
        #     x2 = int(x0 - 1000 * (-b))
        #     y2 = int(y0 - 1000 * a)
        #     cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # if len(g2) != 0:
        #     g2_theta_average = np.average([a[0][1] for a in g2])
        #     g2_r_average = np.average([a[0][1] for a in g2])
        #     a = np.cos(g2_theta_average)
        #     b = np.sin(g2_theta_average)
        #     x0 = a * g2_r_average
        #     y0 = b * g2_r_average
        #     x1 = int(x0 + 1000 * (-b))
        #     y1 = int(y0 + 1000 * a)
        #     x2 = int(x0 - 1000 * (-b))
        #     y2 = int(y0 - 1000 * a)
        #     cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('img', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
