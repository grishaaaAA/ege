f = open('inf_22_10_20_26 (1).txt')
n = int(f.readline())
s = 0
maxi = 0
a = []
for i in f:
    x = int(i)
    if x <= 100:
        s += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a)//2:
        s += a[i] * 0.70
        maxi = a[i]
    else:
        s += a[i]
print(round(s), maxi)