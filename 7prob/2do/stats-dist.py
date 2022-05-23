import stats

x = [0.0, 0.25, 1.25, 1.75, 2.5, 2.7]
y = [1.5 * x for x in x]

print(stats.linr(x, y))
