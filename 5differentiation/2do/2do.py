#
# refer to PPT file
# for exercise
#
from scipy.misc import derivative
from math import sin

def f(x):
    return (sin(2 * x) ** 3) / (x ** 4 + 1)


print(derivative(f, 2.45))
