import math


def handler(q):
    count = 0
    left = -57.5 + (3306 + q) ** 0.5
    left = math.ceil(left)
    right = q ** 0.5
    right = math.floor(right)
    for divider in range(left, right + 1):
        if q % divider == 0:
            count += 1
    if count >= 3:
        print(q)


def okk():
    for n in range(2*10**6, 3*10**6 + 1):
        handler(n)

okk()
