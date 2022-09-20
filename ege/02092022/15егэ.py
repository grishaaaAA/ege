def f(x, a):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))


def task():
    for a in range(32):
        if all([f(x, a) for x in range(32)]):
            print(a)
            return


task()
