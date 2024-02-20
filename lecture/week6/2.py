def f():
    yield 1
    yield 2
    yield 3

g1 = f()
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))