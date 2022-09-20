def f(x, l, r):
    return ((5 <= x <= 30) == (14 <= x <= 23)) <= (not (l < x < r))


def task():
    maxlength = 0
    for l in range(5, 31):
        for r in range(l, 31):
            if all(f(x, l, r) for x in range(5, 31)):
                maxlength = max(maxlength, r - l)
    print(maxlength)


task()
