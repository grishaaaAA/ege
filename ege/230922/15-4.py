def f(x, a):
    return (a % 45 == 0) and ((750 % x == 0) <= ((a % x != 0) <= (120 % x != 0)))


def task():
    for a in range(1, 1000):
        if all([f(x, a) for x in range(1, 1000)]):
            print(a)
            return


task()
