def f(x, y):
    if x + y > 1:
        while x > 0:
            x = x + x + y
            y = y - 1
    return None