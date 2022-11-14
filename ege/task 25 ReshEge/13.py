for n in range(489421, 489440):
    count = 0
    deviders = []
    for dev in range(1, n + 1):
        if n % dev == 0:
            count += 1
            deviders.append(dev)
        if count > 4:
            break
    if count == 4:
        print(deviders)
