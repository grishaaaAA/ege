def f(s):
    n = 4
    while s < 37:
        s = s + 3
        n = n * 2
    return n


def task():
    for s in range(1, 1000):
        print(s, f(s))


task()
