f = open('17 (1).txt')
n = 10**4
x = [int(f.readline()) for _ in range(n)]
count = 0
maxsum = 0
for l in range(n - 1):
    for r in range(l + 1, n):
        if (x[l] % 7 == 0 or x[r] % 7 == 0) and x[l] % 160 != x[r] % 160:
            count += 1
            maxsum = max(maxsum, x[l] + x[r])
print(count, maxsum)


# time ~ (n**2 - n) / 2 * 6 ~ n**2
# memory ~ n + 5 ~ n