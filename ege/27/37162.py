f = open('27_A (2).txt')
x = [int(f.readline()) for _ in range(int(f.readline()))]
maxSum = 0
minLength = 10**9
for l in range(len(x)):
    for r in range(l, len(x)):
        currentSum = sum(x[l: r + 1])
        if currentSum % 89 == 0:
            if currentSum > maxSum:
                maxSum = currentSum
                minLength = r - l + 1
            elif currentSum == maxSum:
                minLength = min(minLength, r - l + 1)
print(minLength)
