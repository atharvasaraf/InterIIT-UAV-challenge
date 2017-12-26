# my keyboard libraries
from keyboard import Keyboard as kb
# external libraries imported
import numpy as np
import cv2
import qrtools
import os

# Keyboard instance called
inkey = kb()
# qr instance called
# qr = qrtools.QR()

# my variables
thresholdValue = 0;

# my objects
cap = cv2.VideoCapture(0)
while True:
    k=inkey()
    if k!='':
        if ord(k)==119 :
            if thresholdValue <255:
                thresholdValue  +=1
                print thresholdValue
            else :
                print "Max threshold attained with threshold : " + str(thresholdValue)
        elif ord(k)==115 :
            if thresholdValue >0 :
                thresholdValue  -=1
                print thresholdValue
            else :
                print "Min threshold attained with threshold : " + str(thresholdValue)
        else :
            break
    else:
        print ""
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)


    # grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # retval, threshold = cv2.threshold(grayscaled, thresholdValue, 255, cv2.THRESH_BINARY)
    # th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


    # cv2.imshow('frame',frame)
    # cv2.imshow('threshold',threshold)
    # cv2.imshow('th',th)
    # cv2.imwrite('img.png',threshold)
    # if qr.decode('img.png'):
        # print qr.data
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows
# os.remove("img.png")
