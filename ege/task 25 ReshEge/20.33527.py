for n in range(101000000, 102000000 + 1):
    if n % 2 == 0:
        count = 1
        for div in range(2, int(n ** 0.5) + 1):
            if n % div == 0:
                if div % 2 == 0:
                    count += 1
                d = n // div
                if d % 2 == 0:
                    count += 1
                if count > 3:
                    break
        if count == 3:
            print(n)


