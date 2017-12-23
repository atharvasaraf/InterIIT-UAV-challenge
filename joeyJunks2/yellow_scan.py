import cv2, numpy as np

cap = cv2.VideoCapture(1)
lower_colour = np.array([20, 45, 80])
upper_colour = np.array([40, 130, 220])
while True:
    _, frame = cap.read()
    # hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blur = cv2.GaussianBlur(hsv, (15, 15), 0)
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours):
        filter(lambda a: cv2.contourArea(a) > 500, contours)
        c = sorted(contours, key=cv2.contourArea)[::-1]
        for contour in c[0:1:]:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, ((2 * x + w) / 2, (2 * y + h) / 2), 7, (0, 0, 255), -1)
            cv2.putText(frame, "center", ((2 * x + w) / 2 - 20, (2 * y + h) / 2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 255), 2)

        # if cv2.contourArea(c) >= 500:
        #     cv2.drawContours(frame, c, 0, (0, 0, 255), 4)
        #     x, y, w, h = cv2.boundingRect(c[0])
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #     cv2.circle(frame, ((2 * x + w) / 2, (2 * y + h) / 2), 7, (0, 0, 255), -1)
        #     cv2.putText(frame, "center", ((2 * x + w) / 2 - 20, (2 * y + h) / 2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        #                 (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    k = cv2.waitKey(1)
    if k == 27:
        break
    else:
        # print k
        pass
cap.release()
cv2.destroyAllWindows()
