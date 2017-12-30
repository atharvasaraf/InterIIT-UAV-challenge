import math


def getPoint(r1, theta1, r2, theta2):
    ct1 = math.cos(theta1)
    st1 = math.sin(theta1)
    ct2 = math.cos(theta2)
    st2 = math.sin(theta2)
    d = ct1 * st2 - st1 * ct2
    if d != 0.0:
        x = int((st2 * r1 - st1 * r2) / d)
        y = (int)((-ct2 * r1 + ct1 * r2) / d);
        return [x, y]
    else:
        return []


print getPoint(1, 90, 1, 81)
