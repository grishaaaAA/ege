f =open('28130_B.txt')
n = int(f.readline())
r50 = [0]*80
r49 = [0]*80
for _ in range(n):
    x = int(f.readline())
    r = x%80
    if x > 50:
        r50[r] += 1
    else:
        r49[r] += 1
ans = r50[0] * (r50[0] - 1) // 2 + r50[40] * (r50[40] - 1) // 2
for r in range(1, 40):
    ans += r50[r] * r50[80 - r]
for r in range(80):
    ans += r50[r] * r49[(80 - r) % 80]
print(ans)


