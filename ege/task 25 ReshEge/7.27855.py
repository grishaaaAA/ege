for n in range(95632, 95700):
    count = 0
    deviders = []
    for div in range(2, n +1, 2):
        if n % div == 0:
            count += 1
            deviders.append(div)
        if count > 6:
            break
    if count == 6:
        print(deviders)

