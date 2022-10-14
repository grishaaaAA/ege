def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    ans = 0
    if start % 10 != 0:
        ans += f(start + start % 10, end)
    if start >= 20:
        ans += f(start * int(str(start)[0]), end)
    l = [int(x) for x in str(start)]
    r = max(l) - min(l)
    if r != 0:
        ans += f(start + r, end)
    return ans



print(f(21, 62))









