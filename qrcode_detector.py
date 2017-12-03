import cv2
import numpy
import qrtools
import os

qr = qrtools.QR()


thresholdMinValue = 0;
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # retval, threshold = cv2.threshold(grayscaled, 60, 255, cv2.THRESH_BINARY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    # thresholdMinValue +=1
    # print(thresholdMinValue)
    # if thresholdMinValue == 255:
    #     thresholdMinValue = 0
    cv2.imshow('frame',frame)
    # cv2.imshow('th',th)
    # cv2.imshow('threshold',threshold)
    cv2.imwrite('img.png',frame)
    if qr.decode('img.png'):
        print qr.data
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows
os.remove("img.png")
