import math

a = 3
b = 4
c = 5

s = (a + b + c) / 2 # semiperimeter

radius = math.sqrt(s * (s - a) * (s - b) * (s - c)) / s

print(radius)
