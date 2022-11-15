for n in range(110203, 110245):
    count = 0
    deviders = []
    for div in range(2, n + 1, 2):
        if n % div ==0:
            count += 1
            deviders.append(div)
        if count > 4:
            break
    if count == 4:
        print(deviders)