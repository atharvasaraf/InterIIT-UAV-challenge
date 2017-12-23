import cv2, numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    k = cv2.waitKey(1)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)
    cv2.imshow('Detected', frame)
    if k == 27:
        break
    else:
        pass


cap.release()
cv2.destroyAllWindows()
