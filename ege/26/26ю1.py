f = open('26 (643456.txt')
n = int(f.readline())
a = [int(f.readline()) for _ in range(n)]
count = 0
while len(a) != 0:
    if 100 - a[0] in a:
        count += 1
        a.remove(100 - a[0])
    a.remove(a[0])
print(count)



