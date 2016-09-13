import math


def perimeter(x_ords, y_ords):
    perimeter = 0
    for i in range(len(x_ords)):
        perimeter += math.hypot(
            x_ords[i] - x_ords[i-1],
            y_ords[i] - y_ords[i-1])
    return perimeter
