f = open('28129_A (1).txt')
n = int(f.readline())
r7 = [0]*160
r0 = [0]*160
for _ in range(n):
    x = int(f.readline())
    r = x %160
    if x % 7 == 0 and r7[r] < x:
        r7[r] = x
    elif x % 7 != 0 and r0[r] < x:
        r0[r] = x
r7.sort(reverse=True)
r0.sort(reverse=True)
print(r7[0], r7[1])
print(r7[0], r0[0])
print(r7[0], r0[1])
print(r7[1], r0[0])
print(r7[1], r0[1])

