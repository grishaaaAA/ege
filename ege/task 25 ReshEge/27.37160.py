count = 0
for n in range(500000, 600000):
    for div in range(18, n//2 + 1):
        if n % div == 0 and div % 10 == 8:
            count += 1
            print(n, div)
            break
    if count == 5:
        break