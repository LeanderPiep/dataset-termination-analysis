def f(x, y, n):
    while x > 0 and x < n:
        x = -x + y - 5
        y = 2 * y
    return None