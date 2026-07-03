def f(x, y, oldx):
    while x >= 0 or y >= 0:
        oldx = x
        x = y - 1
        y = oldx - 1
    return None