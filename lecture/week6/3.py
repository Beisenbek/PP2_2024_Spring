def f(n):
    a, b = 0, 1
    cnt = 2
    yield a
    while cnt < n:
        yield b
        c = a + b
        a = b
        b = c
        cnt = cnt + 1


for i in f(50):
    print(i)