def rec_sum(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + rec_sum(n // 10)