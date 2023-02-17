def isPrime(n):
    for divider in range(2, int(n**0.5) + 1):
        if n % divider == 0:
            return False
    return n != 1



def ok():
    for p in range(155, 165):
        if isPrime(p):
            print(p**4, (p**3 + p**2 + p))
ok()