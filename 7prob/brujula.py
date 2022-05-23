from random import choice

def brujula():
    return choice(['norte', 'sur', 'este', 'oeste'])


print(brujula())
print(brujula())
print(brujula())
print(brujula())


def throwCoin():
    return choice(['aguila', 'sello'])

def evaluateCoinThrows(times):
    values = {}
    for iteration in range(times):
        coin = throwCoin()
        values[coin] = values.get(coin, 0) + 1
    return values

print(evaluateCoinThrows(20))
print(evaluateCoinThrows(40))

