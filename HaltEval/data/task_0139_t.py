def f(x, y):
    x = abs(x)
    y = abs(y)
    while y > 0:
        r = x
        while r >= y:
            r = r - y
        x = y
        y = r
    return None