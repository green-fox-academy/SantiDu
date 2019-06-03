numbers = (1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14)

even_numbers = filter(lambda n: n % 2 == 0, numbers)

print(tuple(even_numbers))

