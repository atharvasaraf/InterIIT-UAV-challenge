import cv2, numpy as np

cap = cv2.VideoCapture(0)
template1 = cv2.imread('haz.png')
template = cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)
while True:
    ret, frame = cap.read()
    # img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # w, h = template.shape[::-1]
    # res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # threshold = 0.6
    # loc = np.where(res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv2.imshow('Detected', template)

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