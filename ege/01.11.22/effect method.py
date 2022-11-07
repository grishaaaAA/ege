import math


def handler(q):
    count = 0
    left = -50 + (25 * 10 ** 2 + q) ** 0.5
    left = math.ceil(left)
    right = q ** 0.5
    right = math.floor(right)
    for divider in range(left, right + 1):
        if q % divider == 0:
            count += 1
    if count >= 3:
        print(q)


def effectMethod():
    for n in range(10**6, 2*10**6 + 1):
        handler(n)


effectMethod()
#18


