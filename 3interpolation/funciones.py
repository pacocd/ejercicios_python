from math import exp


def fn(x):
    return x - exp(2 * x) + 4

def ck(a, b):
    numerator = fn(b) * a - fn(a) * b
    denominator = fn(b) - fn(a)

    return numerator / denominator

print(ck(0.5, 1))
