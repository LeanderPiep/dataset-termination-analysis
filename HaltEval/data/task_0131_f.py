def f(x, y):
    while x <= y and y > 0:
        x = (x - 1) & y
    return None