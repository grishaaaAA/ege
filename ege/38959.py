def ok(n):
    count = 0
    product = 1
    for divider in range(2, n + 1):
        if n % divider == 0:
            count += 1
            product *= divider
            if product >= n:
                return False
            if count == 5:
                print(product)
                return True

    return False




