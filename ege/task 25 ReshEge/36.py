for d in range(10):
    for s in range(1000):
        x = int(f'1{d}2139{s}4')
        if x%2023 == 0:
            print(x, x/2023)
