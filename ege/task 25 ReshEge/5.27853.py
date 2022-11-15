for n in range(312614, 312652):
    count = 0
    deviders = []
    for div in range(1, n + 1):
        if n % div == 0:
            count += 1
            deviders.append(div)
        if count > 6:
            break
    if count == 6:
        print(deviders)