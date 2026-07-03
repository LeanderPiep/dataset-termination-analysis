def f(x, y):
    while x - y > 0:
        x = y - x
        y = y + 1
    return None