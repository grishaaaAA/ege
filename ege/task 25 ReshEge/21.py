def ok(n):
    count = 0
    root = int(n**0.5)
    if root % 2 == 1 and n % root == 0:
        count += 1

    for divider in range(1, root):
        if n % divider == 0:
            if divider % 2 == 1:
                count += 1
            if (n // divider) % 2 == 1:
                count += 1
            if count > 5:
                return False

    return count == 5


def task():
    for n in range(35*10**6, 40*10**6 + 1):
        if ok(n):
            print(n)

task()