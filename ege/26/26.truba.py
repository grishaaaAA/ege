f = open('26 (9).txt')
n = int(f.readline())
truba = [[int(x) for x in f.readline().split()] for _ in range(n)]
ans = [truba[0]]
for i in range(1, n):
    if truba[i][0] + truba[i][1]*2 > ans[-1][0] - ans[-1][1]*2 - 3:
        continue
    ans += [truba[i]]
print(len(ans), ans[-1])




