def isPrime(n):
    for divider in range(2, int(n**0.5) + 1):
        if n % divider == 0:
            return False
    return n != 1


def fiveDeviders():
    for p in range(3, 79 + 1, 2):
        if not isPrime(p):
            continue
        for twoPower in range(0, 25 + 1):
            x = 2**twoPower * p**4
            if 35* 10**6 <= x <= 40 * 10**6:
                print(x)
                break


fiveDeviders()








