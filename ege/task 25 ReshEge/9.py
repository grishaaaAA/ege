max = 0
for n in range(84052, 84131):
    count = 0
    for div in range(1, n + 1):
        if n % div == 0:
            count += 1
    if count > max:
        max = count
        min = n
print(max, min)