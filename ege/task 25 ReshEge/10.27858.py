max = 0
for n in range(120115, 120201):
    count = 0
    for j in range(1, n + 1):
        if n % j == 0:
            count += 1
    if count >= max:
        max = count
        maxnum = n
print(max, maxnum)