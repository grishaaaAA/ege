f = open('26 (11).txt')
n = int(f.readline())
boxs = sorted([int(f.readline()) for _ in range(n)], reverse=True)
ans = [boxs[0]]
for i in range(1, n):
    if boxs[i] > ans[-1] - 3:
        continue
    ans += [boxs[i]]
print(len(ans), ans[-1])
