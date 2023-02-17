# time n(n-1) / 2  memory n
f = open('')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
maxProduct = 0
for l in range(len(x) - 1):
    for r in range(l + 1, len(x)):
        a, b = x[l], x[r]
        if (a * b) % 14 == 0:
            maxProduct = max(maxProduct, a * b)
print(maxProduct)
