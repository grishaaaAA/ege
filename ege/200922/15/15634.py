def f(x, y, a):
    return (y + 2*x < a) or (x > 30) or (y > 20)


def task():
    for a in range(1000):
        r = True
        for x in range(1000):
            for y in range(1000):
                r = r and f(x, y, a)
        if r:
            print(a)
            return


task()
