f = open('24_demo.txt')

currentLength = 1
maxLength = 0
previous = f.read(1)
while True:
    next = f.read(1)
    if next == '':
        maxLength = max(maxLength, currentLength)
        break
    if previous != next:
        currentLength += 1
    else:
        maxLength = max(maxLength, currentLength)
        currentLength = 1
    previous = next

print(maxLength)


# time ~ 2n
# memory ~ const



