def mode(array):
    values = {}
    for value in array:
        values[value] = values.get(value, 0) + 1
    higherValue = max(values.values())

    return [key for key, value in values.items() if value == higherValue]


print(mode([1, 2, 3, 4, 4, 4, 3]))
print(mode([1, 3, 3, 4, 4, 4, 3]))
