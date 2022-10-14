f = open('242.txt')
s = f.read()
currentLength = 0
maxLength = 0
for i in range(len(s)):
    if s[i] == 'X':
        currentLength += 1
    else:
        maxLength = max(currentLength, maxLength)
        currentLength = 0
maxLength = max(currentLength, maxLength)

print(maxLength)
