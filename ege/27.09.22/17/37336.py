f = open('17.txt')
n = 5000
count = 0
maxsum = 0
x = [int(f.readline()) for _ in range(n)]
for i in range(n - 1):
    if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
        count += 1
        maxsum = max(maxsum, x[i] + x[i + 1])
print(count, maxsum)

# time python ~ 10**7 per sec
# time ~ n + 4(n-1) = 5n-4 ~ n
# memory ~ n + 5