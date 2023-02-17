f = open('27991_B (3).txt')
n = int(f.readline())
max171, max172, max171sh, max172sh, max2, max2sh = [0]*6
for _ in range(n):
    x = int(f.readline())
    if x % 17 == 0 and x % 2 == 0:
        if max172 < x <= max171:
            max172 = x
        elif x > max171:
            max172, max171 = max171, x
    elif x % 17 == 0 and x % 2 != 0:
        if max172sh < x <= max171sh:
            max172sh = x
        elif x > max171sh:
            max172sh, max171sh = max171sh, x
    elif x % 2 == 0 and x % 17 != 0:
        max2 = max(max2, x)
    elif x % 2 != 0 and x % 17 != 0:
        max2sh = max(max2sh, x)
print(max171,max172)
print(max171, max2)
print(max171sh,max172sh)
print(max171sh,max2sh)







