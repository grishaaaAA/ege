f = open('28129_B.txt')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
A, B = 0, 0
for t in range(len(x)-1):
    for r in range(t +1, len(x)):
        a, b = x[t],x[r]
        if (a % 160 != b % 160) and (a%7 == 0 or b % 7 == 0):
            if a + b > A + B:
                A, B = a, b
print(A, B)