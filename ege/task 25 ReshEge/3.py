for n in range(210235, 210300):
    count = 0
    deviders = []
    for divaders in range(2, n // 2 + 1):
        if n % divaders == 0:
            count += 1
            deviders.append(divaders)
        if count > 4:
            break
    if count == 4:
        print(deviders)


