f = open('28131_B.txt')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
maxA = 0
maxB = 0
for t in range(len(x)-1):
    for r in range(t + 1, len(x)):
        if (t<r) and (x[t]>x[r]) and (x[t] + x[r])% 120 == 0:
            if x[t] + x[r]>maxA+maxB:
                maxA, maxB = x[t], x[r]
print(maxA, maxB)

