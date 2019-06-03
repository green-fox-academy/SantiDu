numbers = (1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14)

squared_positives = map(lambda n: n**2, filter(lambda n: n > 0, numbers))

print(tuple(n for n in squared_positives))