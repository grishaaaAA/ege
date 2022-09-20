n = 125**4 + 25**8 - 30
n6 = ''
while n != 0:
    n6 = str(n % 5) + n6
    n //= 5
print(n6.count('4'))
