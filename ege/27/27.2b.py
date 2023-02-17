f = open('27.5.fipi.txt')
n = int(f.readline())
max141, max142, max2, max7, max0 = [0]*5

for _ in range(n):
    x = int(f.readline())
    if x % 7 == 0 and x % 2 != 0:
        max7 = max(max7, x)
    elif x % 7 != 0 and x % 2 == 0:
        max2 = max(max2, x)
    elif x % 7 != 0 and x % 2 != 0:
        max0 = max(max0, x)
    elif x % 2 == 0 and x % 7 == 0:
        if max142 < x <= max141:
            max142 = x
        elif x > max141:
            max142, max141 = max141, x
print(max([max2 * max7] + [max141 * x for x in [max141, max0, max2, max7]]))

