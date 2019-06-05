def bunnies_again(n):
    if n == 1:
        return 2
    elif n == 0:
        return 0
    if n % 2 == 0:
        return 3 + bunnies_again(n - 1)
    if n % 2 == 1:
        return 2 + bunnies_again(n - 1)