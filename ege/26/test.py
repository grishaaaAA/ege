def too_much_memory_niger():
    f = open('26 (7).txt')
    n = 10**4
    screen = [[0] * n for _ in range(n)]
    for _ in range(int(f.readline())):
        r, c, sign = [x for x in f.readline().split()]
        r = int(r)
        c = int(c)
        if sign == '+':
            screen[r - 1][c - 1] = 1
        else:
            screen[r - 1][c - 1] = 0
    max_count = 0
    ans = -1
    for i in range(n):
        count = screen[i].count(1)
        if count >= max_count:
            max_count = count
            ans = i + 1
    print(ans)

too_much_memory_niger()
# answer is good