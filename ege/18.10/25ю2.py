def handler(n, f):
    dividers = []
    for divider in range(2, n):
        if n % divider == 0:
            dividers.append(divider)
    if len(dividers) == 2:
        #s = str(dividers[0]) + ';' + str(dividers[1]) + ';' +\
         #   str(dividers[0] * dividers[1]) + '\n'
        s = f'{dividers[0]};{dividers[1]};{dividers[0] * dividers[1]}\n'
        f.write(s)


def task():
    f = open('haha.csv', 'w')
    for n in range(174457, 174505 + 1):
        handler(n, f)

task()
