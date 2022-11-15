count = 0
n = 500000001
while count < 5:
    div = 1
    countDiv = 0
    for devider in range(2, n // 2 + 1):
        if n % devider == 0:
            countDiv += 1
            div *= devider
            if div > n:
                break
            if countDiv == 5:
                print(div)
                count += 1
                break
    n += 1