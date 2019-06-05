def rec_add(n):
    if n == 0:
        return 0
    else:
        return n + rec_add(n - 1)