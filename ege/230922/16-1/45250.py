def f(n):
    if n < 3:
        return 2
    if n % 2 == 0 and n > 2:
        return f(n - 2) + f(n - 1) - n
    if n % 2 != 0 and n > 2:
        return f(n - 1) - f(n - 2) + n * 2


print(f(32))

