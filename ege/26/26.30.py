f = open('26 (6).txt')
n = int(f.readline())
length = 604800
a = [0]*(length+1)
globalStart = 1633305600
for k in range(n):
    if k % 1000 == 0:
        print(k)
    start, end = [int(x) for x in f.readline().split(' ')]
    if end == 0:
        end = globalStart + length + 1
    if end < globalStart or start > globalStart + length:
        continue
    if start < globalStart:
        start = globalStart
    if end > globalStart + length:
        end = globalStart + length
    start, end = start - globalStart, end - globalStart

    for i in range(start, end + 1):
        a[i] += 1





