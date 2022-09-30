def ege():
    f = open('17 (1).txt')
    d = 160
    x = [0] * 160
    y = [0] * 160
    n = 10**4
    for _ in range(n):
        a = int(f.readline())
        r = a % 160
        if a % 7 == 0:
            x[r] = max(x[r], a)
        else:
            y[r] = max(y[r], a)
    x.sort()
    x.reverse()
    y.sort()
    y.reverse()
    m71, m72 = x[0], x[1]
    m01, m02 = y[0], y[1]
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

# time ~ 2n + 2nlog_2(n)
# memory ~ 320 int


ege()
