from math import exp

def getRoot():
    iterationValue = 0
    for iteration in range(5):
        result = newton(iterationValue)
        print(f'Iteration result({iteration}): {result}')
        iterationValue = result
    return iterationValue

def newton(x):
    original = exp(2 - x) - 7 * x
    derivative = -exp(2 - x) - 7
    return x - original / derivative

print(f'Result: {getRoot()}')
