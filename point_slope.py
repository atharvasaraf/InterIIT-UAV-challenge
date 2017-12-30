import numpy as np, math


def draw_line_from_point_slope(angle,point,length):
    point = np.array(point)
    result_points = np.zeros(shape=(2, 2))
    result_points[0] = [(point[0] + length * math.cos(math.radians(point[0]))),
                        (point[1] + length * math.sin(math.radians(angle)))]
    result_points[1] = [(point[0] - length * math.cos(math.radians(point[0]))),
                        (point[1] - length * math.sin(math.radians(angle)))]
    return result_points
