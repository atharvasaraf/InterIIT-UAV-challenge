import cv2, numpy as np

cap = cv2.VideoCapture(1)

lower_colour = np.array([30, 100, 50])
upper_colour = np.array([255, 255, 180])

while True:
    ret, frame = cap.read()
    # hue saturation value
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    # cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == 113:
        if lower_colour[0] < 255:
            lower_colour[0] += 1
            print "lower_colour hue : ", lower_colour[0]
        else:
            print "Max lower_colour hue"
    elif k == 97:
        if lower_colour[0] > 0:
            lower_colour[0] -= 1
            print "lower_colour hue: ", lower_colour[0]
        else:
            print "Min lower_colour hue"
    elif k == 119:
        if lower_colour[1] < 255:
            lower_colour[1] += 1
            print "lower_colour saturation : ", lower_colour[1]
        else:
            print "Max lower_colour saturation"
    elif k == 115:
        if lower_colour[1] > 0:
            lower_colour[1] -= 1
            print "lower_colour saturation: ", lower_colour[1]
        else:
            print "Min lower_colour saturation"
    elif k == 101:
        if lower_colour[2] < 255:
            lower_colour[2] += 1
            print "lower_colour value : ", lower_colour[2]
        else:
            print "Max lower_colour value"
    elif k == 100:
        if lower_colour[2] > 0:
            lower_colour[2] -= 1
            print "lower_colour value: ", lower_colour[2]
        else:
            print "Min lower_colour value"
    elif k == 114:
        if upper_colour[0] < 255:
            upper_colour[0] += 1
            print "upper_colour hue : ", upper_colour[0]
        else:
            print "Max upper_colour hue"
    elif k == 102:
        if upper_colour[0] > 0:
            upper_colour[0] -= 1
            print "upper_colour hue: ", upper_colour[0]
        else:
            print "Min upper_colour hue"
    elif k == 116:
        if upper_colour[1] < 255:
            upper_colour[1] += 1
            print "upper_colour saturation : ", upper_colour[1]
        else:
            print "Max upper_colour saturation"
    elif k == 103:
        if upper_colour[1] > 0:
            upper_colour[1] -= 1
            print "upper_colour saturation: ", upper_colour[1]
        else:
            print "Min upper_colour saturation"
    elif k == 121:
        if upper_colour[2] < 255:
            upper_colour[2] += 1
            print "upper_colour value : ", upper_colour[2]
        else:
            print "Max upper_colour value"
    elif k == 104:
        if upper_colour[2] > 0:
            upper_colour[2] -= 1
            print "upper_colour value: ", upper_colour[2]
        else:
            print "Min upper_colour value"
    else:
        pass

hsv_file = open('hsv.txt', 'w')
hsv_file.write(str(lower_colour) + "\n" + str(upper_colour))
hsv_file.close()
cap.release()
cv2.destroyAllWindows()
