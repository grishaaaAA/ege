def realtimetowomax():
    n = int(input())
    max1 = 0
    max2 = 0
    for _ in range(n):
        x = int(input())
        if max2 < x <= max1:
            max2 = x
        elif x > max1:
            max2, max1 = max1, x
    print(max2, max1)


def realtimetowomaxcondition():
    n = int(input())
    max1 = 0
    max2 = -1
    d = 160
    for _ in range(n):
        x = int(input())
        if max2 < x <= max1 and x % d != max1 % d:
            max2, max1 = x, max1
        elif x > max1:
            if x % d != max1 % d:
                max2, max1 = max1, x
            elif x % d != max2 % d:
                max2, max1 = max2, x

    print(max2, max1)


def t37337():
    f = open('17 (1).txt')
    n = 10**4
    d = 160
    p = 7
    m71, m72 = 0, -1
    m01, m02 = 0, -1
    for _ in range(n):
        x = int(f.readline())
        if x % p == 0:
            if m72 < x <= m71 and x % d != m71 % d:
                m72, m71 = x, m71
            elif x > m71:
                if x % d != m71 % d:
                    m72, m71 = m71, x
                elif x % d != m72 % d:
                    m72, m71 = m72, x
        elif x % p != 0:
            if m02 < x <= m01 and x % d != m01 % d:
                m02, m01 = x, m01
            elif x > m01:
                if x % d != m01 % d:
                    m02, m01 = m01, x
                elif x % d != m02 % d:
                    m02, m01 = m02, x

    x, y = m71, m72
    if m71 + m01 > x + y and m71 % d != m01 % d:
        x, y = m71, m01
    if m71 + m02 > x + y and m71 % d != m02 % d:
        x, y = m71, m02
    if m72 + m01 > x + y and m72 % d != m01 % d:
        x, y = m72, m01
    if m72 + m02 > x + y and m72 % d != m02 % d:
        x, y = m72, m02
    print(x, y, x + y)

    # time ~ n
    # memory ~ 1


t37337()
