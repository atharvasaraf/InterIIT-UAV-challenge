import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 100, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(frame_hsv, lower_red, upper_red)
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, ((2*x+w)/2, (2*y+h)/2), 7, (255, 255, 255), -1)
        cv2.putText(frame, "center", ((2*x+w)/2 - 20, (2*y+h)/2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 2)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == -1:
        pass
        # elif k == 82 :
        #     if thresholdValue <255 :
        #         thresholdValue += 1
        #         print "threshold : ",thresholdValue
        #     else :
        #         print "Max threshold"
        # elif k == 84 :
        #     if thresholdValue >0 :
        #         thresholdValue -= 1
        #             print "threshold : ",thresholdValue
        #         else :
        #             print "Min threshold"
    else:
        # print k
        pass

cap.release()
cv2.destroyAllWindows()
