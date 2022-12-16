def last_hope():
    f = open('26 (7).txt')
    n = 100000
    screen = [set() for _ in range(n + 1)]
    for _ in range(int(f.readline())):
        r, c, sign = f.readline().split()
        r = int(r)
        c = int(c)
        if sign == '+':
            screen[r].add(c)
        elif c in screen[r]:
            screen[r].remove(c)
    max_count = 0
    ans = -1
    for i in range(n):
        count = len(screen[i])
        if count >= max_count:
            max_count = count
            ans = i
    print(max_count, ans)

last_hope()
# answer is good niger




