import cv2,numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    # hue saturation value
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([40,0,0])
    upper_red = np.array([80,255,255])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("mask",mask)
    cv2.imshow("res", res)
    k=cv2.waitKey(1)
    if k == 27 :
        break
    elif k == -1 :
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
    else :
        print K
        # pass
cap.release()
cv2.destroyAllWindows
