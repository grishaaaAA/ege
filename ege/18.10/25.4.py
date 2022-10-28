def amountOfNotTrivialDividers(n):
    count = 0
    maxDivider = 0
    for divider in range(2, n // 2 + 1):
        if n % divider == 0:
            count += 1
            maxDivider = divider
    return [count, maxDivider]


def amountOfNotTrivialDividersSqrt(n):
    count = 0
    root = int(n**0.5)
    maxDivider = 0
    for divider in range(root - 1, 1, -1):
        if n % divider == 0:
            maxDivider = n // divider
            count += 2
    if n % root == 0:
        count += 1
    return [count, maxDivider]


def task():
    count = 0
    for n in range(123456789, 223456789):
        temp = amountOfNotTrivialDividers(n)
        if temp[0] == 3:
            count += 1
            print(n, temp[1])
    print(count)








a = 0
for i in range(123456789, 223456790):
        s = i ** 0.5
        nn = 0
        if round(s) == s:


    



