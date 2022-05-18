import functools

coordinate1 = (-4, -2)
coordinate2 = (1, 5)

def fn(y, c0, c1):
    a = (c1[0] - c0[0]) / (c1[1] - c0[1])
    b = y - c0[1]

    return a * b + c0[0]

print(fn(3.7, coordinate1, coordinate2))


homework = [(-2, 4), (-1, -2), (3, 5), (4.3, 11)]

def interpolatingPolynomial(x, coordinates):
    mixedCoords = mixCoords(coordinates)
    func = lambda stored, iteration: stored + operation(x, mixedCoords[iteration])
    return functools.reduce(func, range(4), 0)

def mixCoords(coordinates):
    c0, c1, c2, c3 = coordinates
    return [
            coordinates,
            [c1, c0, c2, c3],
            [c2, c0, c1, c3],
            [c3, c0, c1, c2]
        ]

def operation(x, coordinates):
    c0 = coordinates[0]
    return divisionOperation(x, coordinates) * c0[1]

def divisionOperation(x, coordinates):
    x0, x1, x2, x3 = [coordinate[0] for coordinate in coordinates]
    dividend = (x - x1) * (x - x2) * (x - x3)
    divider = (x0 - x1) * (x0 - x2) * (x0 - x3)
    return dividend / divider

# Ejercicio de Tarea

print("Ejercicio de tarea")
print(homework, "x =", 7.7)
print(interpolatingPolynomial(7.7, homework))
