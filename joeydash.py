import cv2, numpy as np, math


class Joeydash:
    def get_landing_point_drift(self,lower_color, upper_color):
        cap = cv2.VideoCapture(0)
        box_location_file = open('box_location.txt', 'w')
        while True:
            _, frame = cap.read()
            height, width = frame.shape[:2]
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            blur = cv2.GaussianBlur(hsv, (15, 15), 0)
            mask = cv2.inRange(hsv, lower_color, upper_color)
            _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours):
                filter(lambda a: cv2.contourArea(a) > 500, contours)
                c = sorted(contours, key=cv2.contourArea)[::-1]
                for contour in c[0:1:]:
                    x, y, w, h = cv2.boundingRect(contour)
                    dist = math.sqrt(w ** 2 + h ** 2)
                    box_location_file.write(
                        str(((2 * x + w) / 2) - (width / 2)) + "\t" + str((height / 2) - ((2 * y + h) / 2)))
            k = cv2.waitKey(1)
            if k == 27:
                break
            else:
                # print k
                pass
        box_location_file.close()

    def get_focal_length(self):
        print "units are in cms\n Press 'q' to increase camera distance\n Press 'a' to decrease camera distance\n " \
              "Press 'w' to increase box diagonal lenght\n Press 'w' to decrease box diagonal lenght "
        cap = cv2.VideoCapture(0)
        cam_height = 5
        box_diagonal_distance = 5
        lower_colour = np.array([20, 45, 80])
        upper_colour = np.array([40, 130, 220])
        while True:
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_colour, upper_colour)
            _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours):
                filter(lambda a: cv2.contourArea(a) > 500, contours)
                c = sorted(contours, key=cv2.contourArea)[::-1]
                for contour in c[0:1:]:
                    x, y, w, h = cv2.boundingRect(contour)
                    dist = math.sqrt(w ** 2 + h ** 2)
                    cv2.putText(frame, "focal length : " + str((dist * cam_height) / box_diagonal_distance),
                                ((2 * x + w) / 2 - 20, (2 * y + h) / 2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 0, 255), 2)
            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif k == 113:
                if cam_height < 1000:
                    cam_height += 1
                    print "cam height : ", cam_height
                else:
                    print "dekh bhai 10 metre jyada hota hain"
            elif k == 97:
                if cam_height > 0:
                    cam_height -= 1
                    print "cam height : ", cam_height
                else:
                    print "are behencho zero se niche nahin jayega"
            elif k == 119:
                if box_diagonal_distance < 1000:
                    box_diagonal_distance += 1
                    print "box diagonal distance: ", box_diagonal_distance
                else:
                    print "dekh bhai 10 metre jyada hota hain"
            elif k == 115:
                if box_diagonal_distance > 0:
                    box_diagonal_distance -= 1
                    print "box diagonal distance : ", box_diagonal_distance
                else:
                    print "are behencho zero se niche nahin jayega"
            else:
                pass

    def get_average_line(self):
        cap = cv2.VideoCapture(0)
        minLineLength = 0.1
        maxLineGap = 10
        while True:
            _, frame = cap.read()
            lower_colour = np.array([20, 45, 80])
            upper_colour = np.array([40, 130, 220])
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_colour, upper_colour)
            edges = cv2.Canny(mask, 50, 150, apertureSize=3)
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 4, minLineLength, maxLineGap)
            if lines is not None:
                all_x1 = np.ones(shape=(len(lines)))
                all_y1 = np.ones(shape=(len(lines)))
                all_x2 = np.ones(shape=(len(lines)))
                all_y2 = np.ones(shape=(len(lines)))
                for i in range(len(lines)):
                    for x1, y1, x2, y2 in lines[i]:
                        all_x1[i] = x1
                        all_y1[i] = y1
                        all_x2[i] = x2
                        all_y2[i] = y2
                cv2.line(frame, (int(np.average(all_x1)), int(np.average(all_y1))), (int(np.average(all_x2)), int(np.average(all_y2))),
                         (0, 255, 0), 2)
            cv2.namedWindow('img', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('img', 1368, 786)
            cv2.imshow('img', frame)

            k = cv2.waitKey(1)
            if k == 27:
                break
            else:
                pass
        cap.release()
cv2.destroyAllWindows()