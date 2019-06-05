def bunnies(n):
    if n == 0:
        return 0
    else:
        return 2 + bunnies(n - 1)