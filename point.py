from math import sqrt, atan

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x, self.y

    def distance(self, p):
        if not isinstance(p, Point): return "Point is required"
        return sqrt(((p.x - self.x) ** 2) + ((p.y - self.y) ** 2))

    def angle(self):
        return atan(self.y / self.x)



p0 = Point(1.0, 2.0)
p1 = Point(2.0, 3.0)

print("P0 distance to P1:", p0.distance(p1))
print("P1 distance to P0:", p1.distance(p0))
print("P1 wrong distance to 1:", p1.distance(1))
print("P1 wrong distance to non-point value:", p1.distance("Value"))
print("P0 angle:", p0.angle())
print("P1 angle:", p1.angle())
print("P0 point:", p0.getPoint())
print("P1 point:", p1.getPoint())
