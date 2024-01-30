def isPrime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt = cnt + 1
    return cnt == 2

l = list(map(int, input().split()))
print([x for x in l if isPrime(x)]) #list comprehension