f = open('28130_A.txt')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
count = 0
for l in range(len(x)):
    for r in range(l + 1, len(x)):
        a, b = x[l], x[r]
        if (a+b) % 80 == 0 and (a>50 or b>50):
            count += 1
print(count)
