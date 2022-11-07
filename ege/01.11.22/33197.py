def handler(n):
    count = 0
    for divider1 in range(int(n**0.5), 0, -1):
        if n % divider1 == 0:
            divider2 = n // divider1
            if divider2 - divider1 <= 100:
                count += 1
            else:
                break
    if count >= 3:
        print(n)


for n in range(10**6, 2*10**6 + 1):
    handler(n)


