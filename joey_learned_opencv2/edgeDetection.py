import cv2, numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    edges = cv2.Canny(frame, 100, 200)

    # cv2.imshow("frame", frame)
    cv2.imshow("edges", edges )

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
