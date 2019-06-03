from functools import reduce

numbers = (1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14)

odd_numbers = tuple(filter(lambda n: n % 2 == 1, numbers))
avg_odd_numbers = reduce(lambda x, y: x + y, odd_numbers) / len(odd_numbers)


print(avg_odd_numbers)
