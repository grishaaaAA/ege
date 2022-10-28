s = open('245.txt').read()
s = s[:-1]
s = s.replace('XYZ', '000')
s = s.replace('0XY', '0001')
s = s.replace('0X', '001')
s = s.replace('0Y', '01')
s = s.replace('0Z', '01')
s = s.replace('Z', '')
s = s.replace('Y', '')
s = s.replace('X', '')
x = s.split('1')
y = [len(z) for z in x]
print(max(y))
#0000000000000000001zyzz00000000000001zzzyzxz000000001zxzy000001
#00000XYXY