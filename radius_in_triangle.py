from math import sqrt

def semiperimeter(a, b, c):
    return (a + b + c) / 2

def calculateCircleRadiusInTriangle(a, b, c):
    area = calculateTriangleArea(a, b, c)

    return area / semiperimeter(a, b, c)

def calculateTriangleArea(a, b, c):
    s = semiperimeter(a, b ,c)

    return sqrt(s * (s - a) * (s - b) * (s - c))

print(calculateCircleRadiusInTriangle(3, 4, 5))
print(calculateCircleRadiusInTriangle(2, 2, 3))
print(calculateCircleRadiusInTriangle(13, 14, 15))
