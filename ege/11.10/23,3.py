def f(start, end):
    if start == 6:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 2, end) + f(start * 3, end)


print(f(1, 25) * f(25, 63))
