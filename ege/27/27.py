f = open('27-A.txt')
n = int(f.readline())

sum_of_max = 0
min_difference = 10001

for _ in range(n):
    x, y = sorted([int(x) for x in f.readline().split()])
    sum_of_max += y
    difference = y - x
    if difference % 3 != 0:
        min_difference = min(min_difference, difference)

if sum_of_max % 3 != 0:
    print(sum_of_max)
elif min_difference != 10001:
    print(sum_of_max - min_difference)
else:
    print('no solution, niger')
