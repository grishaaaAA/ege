def isapproriate(x, y, z):
    x, y, z = sorted([x, y, z])
    if z < x + y:
        return True


def handler(a, b, c, d):
    return isapproriate(b, c, d) and isapproriate(a, c, d) and\
           isapproriate(a, b, d) and isapproriate(a, b, c)


def task():
    f = open('source.csv')

    count = 0
    for _ in range(5000):
        a, b, c, d = [int(x) for x in f.readline().split(';')]
        if handler(a, b, c, d):
            count += 1

    print(count)


task()
