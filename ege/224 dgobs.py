for n in range(228224, 531135 + 1):
    count = 0
    for divider in range(1, int(n**1/3) +1):
        if n % (divider**3) == 0:
            count += 1



