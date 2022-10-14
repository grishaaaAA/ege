f = open('24_demo.txt')

s = f.read()

currentLength = 1
maxLength = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        currentLength += 1
    else:
        maxLength = max(maxLength, currentLength)
        currentLength = 1

maxLength = max(currentLength, maxLength)

print(maxLength)

# time ~ 2n
# memory ~ n