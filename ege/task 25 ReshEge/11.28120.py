for n in range(201455, 201470):
    count = 0
    deviders = []
    for div in range(1, n + 1):
        if n % div == 0:
            count += 1
            deviders.append(div)
        if count > 4:
            break
    if count == 4:
        print(deviders)