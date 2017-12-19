import cv2, numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([40, 0, 0])
    upper_red = np.array([80, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernal = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(frame, -1, kernel=kernal)
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    median = cv2.medianBlur(frame, 15)
    bilateral =cv2.bilateralFilter(frame, 15, 75, 75)

    # cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)
    # cv2.imshow("res", res)
    # cv2.imshow("smoothed", smoothed)
    # cv2.imshow("blur", blur)
    cv2.imshow("median", median)
    cv2.imshow("bilateral", bilateral)

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
cv2.destroyAllWindows
