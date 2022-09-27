f = open('17.txt')
count = 0
maxsum = 0
previous = int(f.readline())
while True:
    next = f.readline()
    if next == '':
        break
    next = int(next)
    if previous % 3 == 0 or next % 3 == 0:
        count += 1
        maxsum = max(maxsum, next + previous)
    previous = next
print(count, maxsum)


# real-time system
# time ~ 7n + 4 ~ n
# memory ~ 4