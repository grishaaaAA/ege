count = 0
n = 10000001
while count < 5:
    div = 0
    countDiv = 0
    for devideer in range(n // 2, 1, -1):
        if n % devideer == 0:
            countDiv += 1
            div += devideer
            if div > 10000:
                break
            if countDiv == 2:
                print(div)
                count += 1
                break
    n += 1