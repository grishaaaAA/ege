def ok(n):
    count = 0
    product = 1
    for divider in range(2, n + 1):
        if n % divider == 0:
            count += 1
            product *= divider
            if product >= n:
                return False
            if count == 5:
                print(product)
                return True

    return False


def task():
    count = 0
    number = 200 * 10**6 + 1
    while count < 5:
        if ok(number):
            count += 1
        number += 1


task()
