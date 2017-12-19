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
        print k
        # pass
cap.release()
cv2.destroyAllWindows()
