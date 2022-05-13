#
# generate a function to produce points 
# to be used as x-axis
# 
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]
#

def customRange(initialValue, finalValue, increment):
    counter = initialValue
    values = []
    while counter <= finalValue:
        values.append(counter)
        counter += increment

    return values


print(customRange(1, 3, 0.1))
print(customRange(5, 7, 0.2))
print(customRange(5, 7, 0.3))
print(customRange(1, 4, 0.7))
