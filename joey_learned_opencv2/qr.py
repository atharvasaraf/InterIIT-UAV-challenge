import cv2
import os
import qrtools

qr = qrtools.QR()

cap = cv2.VideoCapture('rtsp://192.168.1.1:554/MJPG?W=720&H=400&Q=50&BR=5000000/track1')
cap.set(4, 1920)
cap.set(5, 1080)
cap.set(15, 0.1)
i = 1
while True:

    ret, frame = cap.read()

    cv2.imwrite('img.png', frame)
    if qr.decode('img.png'):
        print "data : ", qr.data
        print i
        i += 1
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
# os.remove('img.png')
cv2.destroyAllWindows()
