numbers = (1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14)

any_even = any(filter(lambda x: x % 2 == 0, numbers))

print(any_even)