import math

n = 5000
iter = (n**2 + n) // 2
iter = int(iter * math.log2(n))
print(iter // 10**7)


def binarySearch(x, y):
    l = 0
    r = len(x) - 1
    while l <= r:
        m = (l + r) // 2
        if y == x[m]:
            return m
        elif y < x[m]:
            r = m
        else:
            l = m
    return 'no such element, niger'


x = [11, 22, 33, 44, 55]
print(binarySearch(x, 45))

