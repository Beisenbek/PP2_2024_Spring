def infinite_sequence(start, stop):
    num = start
    while num < stop:
        yield num
        num += 1

for i in infinite_sequence(0, 20):
    print(i, end=" ")