points = [1, 2, 3]

for i in range(2, 0, -1):
    points[i] = points[i - 1]

points[0] = 4

print(points)
