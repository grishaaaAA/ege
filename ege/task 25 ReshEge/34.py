count = 0
n = 460000001
while count < 5:
    countDiv = 0
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            countDiv += 1
            if countDiv == 5:
                print(n // div)
                count += 1
                break
    n += 1