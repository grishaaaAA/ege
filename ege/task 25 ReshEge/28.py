def ok(n):
    for minDivider in range(2, int(n ** 0.5) + 1):
        if n % minDivider == 0:
            m = minDivider + n // minDivider
            if (m != minDivider + 1) and (m % 10 == 8):
                print(n, m)
                return True
    return False


def task():
    count = 0
    number = 700000 + 1
    while count < 5:
        if ok(number):
            count += 1
        number += 1


task()
