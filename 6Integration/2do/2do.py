#a
# 2do
#

# Resolver mediante 2 métodos
# 0∫1.9724 (2sen(√(x - x))) dx -> firstEquation
# -1∫2 (7^(-x) + 3) dx -> secondEquation
from math import sin, sqrt, radians

def firstEquation(x):
    return 2 * sin(sqrt(x)) + (-1 * x)

def secondEquation(x):
    return 7**-x + 3

def rectangleRule(f, a, b):
    return f(a) * (b - a)

def midPointRule(f, a, b):
    return f((a + b) / 2) * (b - a)

def trapezoidalRule(f, a, b):
    return ((b - a) / 2) * (f(a) + f(b))

def simpsonRule(f, a, b):
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) / 2) + f(b))

print("Regla del rectángulo")
print(rectangleRule(firstEquation, 0, 1.9724))
print(rectangleRule(secondEquation, -1, 2))

print("Regla del punto medio")
print(midPointRule(firstEquation, 0, 1.9724))
print(midPointRule(secondEquation, -1, 2))

print("Regla del trapecio")
print(trapezoidalRule(firstEquation, 0, 1.9724))
print(trapezoidalRule(secondEquation, -1, 2))

print("Regla de simpson")
print(simpsonRule(firstEquation, 0, 1.9724))
print(simpsonRule(secondEquation, -1, 2))

