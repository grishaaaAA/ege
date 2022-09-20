def f(x, y, a):
    return ((x < a) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= a))


def task():
    count = 0
    for a in range(500):
        r = True
        for x in range(1000):
            for y in range(1000):
                r = r and f(x, y, a)
        if r:
            count += 1
    print(count)


task()
