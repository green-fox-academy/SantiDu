def com_div(a, b):
    if a % min(a, b) == 0 and b % min(a, b) == 0:
        return min(a, b)
    return com_div(a - 1, b - 1)