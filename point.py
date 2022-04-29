from math import sqrt, atan

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x, self.y

    def distance(self, p):
        if isinstance(p, Point):
            x1 = p.x
            y1 = p.y
            x2 = self.x
            y2 = self.y
            return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        else:
            print("Point is required")

    def angle(self):
        return atan(self.y / self.x)
