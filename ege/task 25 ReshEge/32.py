count = 0
n = 11000001
while count < 5:
    div = 0
    countDiv = 0
    for j in range(n//2, 1, -1):
        if n % j == 0:
            countDiv += 1
            div += j
            if div > 10000:
                break
            if countDiv == 2:
                print(div)
                count += 1
                break
    n += 1