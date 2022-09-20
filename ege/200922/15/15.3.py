def f(x, y, a):
    return ((x <= 9) <= (x**2 <= a)) and ((y**2 <= a) <= (y <= 9))


def task():
    for a in range(500, 1, -1):
        r = True
        for x in range(1000):
            for y in range(1000):
                r = r and f(x, y, a)
        if r:
            print(a)
            return


task()
