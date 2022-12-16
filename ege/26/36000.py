f = open('inf_26_04_21_26.txt')
n = int(f.readline())
x = [int(f.readline()) for _ in range(n)]
s = set(x)
count = 0
maxSumm = 0
for left in range(len(x)-1):
    for right in range(left + 1, len(x)):
        summ = x[left] + x[right]
        if summ % 2 == 1 and summ in s:
            count += 1
            maxSumm = max(maxSumm, summ)
print(count, maxSumm)




