def p(s):
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    # s * 2**8 >= 2050 s >= 2050/256 = 8
    # 8 * 7 = 56
    # 55
    return n


def task():
    for s in range(6, 10**9):
        if p(s) == 60:
            print(s)
            return


task()
# exercise 6
