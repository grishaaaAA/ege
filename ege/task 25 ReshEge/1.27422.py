for n in range(174457, 174505):
    count = 0
    deviders = []
    for divaders in range(2, n // 2 + 1):
        if n % divaders == 0:
            count += 1
            deviders.append(divaders)
        if count > 2:
            break
    if count == 2:
        print(deviders)


