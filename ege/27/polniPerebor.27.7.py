f = open('111')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
A, B = 0, 0
for t in range(len(x)-1):
    for r in range(t +1, len(x)):
        a, b = x[t],x[r]
        if (a-b) % 2 == 0 and (a%17 == 0 or b % 17 == 0):
            if a + b > A + B:
                A, B = a, b
print(A, B)