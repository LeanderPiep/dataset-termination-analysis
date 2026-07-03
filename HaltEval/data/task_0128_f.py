def f(x, y):
    oldx = x
    while x < 5:
        oldx = x
        x = oldx - y
        y = oldx + y
    return None