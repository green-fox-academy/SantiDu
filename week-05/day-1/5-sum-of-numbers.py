from functools import reduce

numbers = (1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14)

even_n_lteq_10 = filter(lambda x: x % 2 == 0 and x <= 10, numbers)

sum_of_numbers = reduce(lambda x, y: x + y, even_n_lteq_10)

print(sum_of_numbers)