import cv2, numpy as np

cap = cv2.VideoCapture(0)
template1 = cv2.imread('haz.png')
template = cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)
while True:
    ret, frame = cap.read()
    cv2.imshow('Detected', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
    else:
        pass


cap.release()
cv2.destroyAllWindows()