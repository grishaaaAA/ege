min = 0
max = 0
for n in range(568023, 569231):
    count = 2
    for div in range(2, n//2 + 1):
        if n % div == 0:
            count += 1
    if count>max:
        max = count
        min = n
print(max, min)