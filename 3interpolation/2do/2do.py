coordinate1 = (-4, -2)
coordinate2 = (1, 5)

def fn(y, c0, c1):
    a = (c1[0] - c0[0]) / (c1[1] - c0[1])
    b = y - c0[1]

    return a * b + c0[0]

print(fn(3.7, coordinate1, coordinate2))
