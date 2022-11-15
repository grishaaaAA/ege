count = 0
n = 600001
while count < 5:
    for div in range(2, n // 2 + 1):
        if n % div == 0 and div % 10 == 7 and div != 7:
            print(n, div)
            count += 1
            break
    n += 1