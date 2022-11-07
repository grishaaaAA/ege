def isPrime(n):
    for divider in range(2, int(n**0.5) + 1):
        if n % divider == 0:
            return False
    return n != 1
#simplicity test

def netrivialDivider():
    for n in range(123456789, 223456789 + 1):
        quadRoot = n**0.25
        if quadRoot % 1 != 0:
            continue
        quadRoot = int(quadRoot)
        if isPrime(quadRoot):
            print(n, quadRoot**3)
#long method

def effective():
    for p in range(107, 122, 2):
        if isPrime(p):
            print(p**3, p**4)

#quick method
effective()
# task 29673, simplicity test; long method after quick method.
