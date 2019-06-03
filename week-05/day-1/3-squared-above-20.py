numbers = (1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14)

squared_above_20 = filter(lambda n: n > 20, map(lambda n: n**2, numbers))

print(tuple(squared_above_20))