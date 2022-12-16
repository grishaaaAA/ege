d = {}
f = open('107_26.txt')
n = int(f.readline())
for _ in range(n):
    row, seat = [int(x) for x in f.readline().split()]
    if row in d.keys():
        d[row] += [seat]
    else:
        d[row] = [seat]

for row in d.keys():
    d[row].sort()

ans = -1
for row in sorted(d.keys(), reverse=True):
    for seat in range(len(d[row]) - 1):
        if d[row][seat + 1] - d[row][seat] == 14:
            print(row, d[row][seat] + 1)
            exit()


print(ans)
