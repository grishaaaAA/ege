def f(s):
    s = int(input())
    s = (s + 1) // 7
    n = 36
    while s < 2050:
       s = s * 2
       n = n + 3
    return n


def task():
    for s in range(1,1000):
        print(s, f(s))


task()