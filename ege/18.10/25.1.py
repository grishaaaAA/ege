def isPrime(n):
    for divider in range(2, int(n**0.5) + 1):
        if n % divider == 0:
            return False
    return n != 1


def task():
    for n in range(245690, 245756 + 1):
        if isPrime(n):
            print(n - 245690 + 1, n)

task()
