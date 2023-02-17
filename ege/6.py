for a in range(300, 0, -1):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (y + 2*x != 99) or (a < x) or (a < y):
                k += 1
    if k == 90_000:
        print(a)
        break