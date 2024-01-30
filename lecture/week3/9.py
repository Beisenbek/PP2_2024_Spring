def myfunc(a, b, c):
  return lambda x : a * x * x + b * x + c

y1 = myfunc(1, 2, 1)

print(y1(12))