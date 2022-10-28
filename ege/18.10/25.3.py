def countDivider(number, f):
    count = 0
    for devider in range(1, number + 1):
        if number % devider == 0:
            count += 1
    return count

def task():
    f = open('hu.csv', 'w')
    for number in range(84052, 84130):
        countDivider(number, f)

task()






