import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == -1:
        pass
    else:
        print k
        # pass


cap.release()
cv2.destroyAllWindows()
