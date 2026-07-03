def f(x, y):
    while x >= 0:
        y = 1
        while y < x:
            y = 2*y
        x = x - 1
    return None