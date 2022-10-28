s = open('24_de.txt').read()
s = s.replace('XYZ', '000')
s = s.replace('0XY', '0001')
s = s.replace('0X', '001')
s = s.replace('Y', '1')
s = s.replace('X', '1')
s = s.replace('Z', '1')
while '11' in s:
    s = s.replace('11', '1')
x = s.split('1')
y = [len(z) for z in x]
print(max(y))

