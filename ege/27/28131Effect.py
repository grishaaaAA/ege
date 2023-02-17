f = open('28131_B.txt')
n = int(f.readline())
r = [0]*120
a, b = 0, 0
for _ in range(n):
    x = int(f.readline())
    rx = x % 120
    pairR = (120 - rx) % 120
    if r[pairR] != 0:
        if x + r[pairR] > a + b and r[pairR] > x:
            a, b = r[pairR], x
    r[rx] = max(r[rx], x)
print(a, b)
