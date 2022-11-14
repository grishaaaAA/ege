for d in range(10):
    for s in range(10):
        x = int(f'12345{d}7{s}8')
        if x%23 == 0:
            print(x, x/23)
