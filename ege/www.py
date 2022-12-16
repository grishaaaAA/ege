for n in range(100000, 500000, 10):
    count = 0
    deviders = []
    for divaders in range(2, n // 2 + 1, 2):
        if n % divaders == 0:
            count += 1
            deviders.append(divaders)
        if count > 150:
            break
    if count == 150:
        print(deviders)


