def isPrime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt = cnt + 1
    return cnt == 2

def filter(l):
    result = []
    for x in l:
        if isPrime(x):
            result.append(x)
    return result

l = list(map(int, input().split()))
print(filter(l))