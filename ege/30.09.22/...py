def ege():
    f = open('17 (1).txt')
    x = [0] * 160
    y = [0] * 160
    n = 10**4
    for _ in range(n):
        a = int(f.readline())
        r = a % 160
        if a % 7 == 0:
            x[r] += 1
        else:
            y[r] += 1
    ans = 0
    for r in range(160):
        ans += x[r] * (sum(x[r+1:]) + sum(y) - y[r])
    print(ans)

# time ~ 2n + 4*160
# memory ~ 320 int

ege()
