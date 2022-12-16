f = open('26 (3).txt')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
s = set(x)
count = 0
maxMean = 0
for l in range(n - 1):
    for r in range(l + 1, n):
        mean = (x[l] + x[r]) // 2
        if x[l] % 2 == 0 and x[r] % 2 == 0 and mean in s:
            count += 1
            maxMean = max(maxMean, mean)
print(count, maxMean)
