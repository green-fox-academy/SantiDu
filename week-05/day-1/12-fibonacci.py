

def fibonacci():
    a, b = 1, 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b

g = fibonacci()

for i in range(20):
    print(next(g))
