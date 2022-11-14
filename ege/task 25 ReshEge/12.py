SerNumb = 0
for n in range(2422000, 2422080 + 1):
    count = 0
    for div in range(2, n // 2 + 1):
        if n % div == 0:
            count += 1
            break
    if count == 0:
        SerNumb += 1
        print(SerNumb, n)