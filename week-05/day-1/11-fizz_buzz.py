def fizz_buzz():
    n = 0
    while True:
        n += 1
        fizz_or_buzz = f"{'Fizz' if n % 3 == 0 else ''}{'Buzz' if n % 5 == 0 else ''}"
        yield n if not fizz_or_buzz else fizz_or_buzz 

g = fizz_buzz()

for i in range(20):
    print(next(g))