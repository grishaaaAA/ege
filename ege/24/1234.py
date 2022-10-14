f = open('242.txt')
s = f.read()
s = s.replace('Y', '0')
s = s.replace('Z', '0')
s = s[:-1]
while '00' in s:
    s = s.replace('00', '0')
x = s.split('0')
y = [len(m) for m in x]
print(max(y))
