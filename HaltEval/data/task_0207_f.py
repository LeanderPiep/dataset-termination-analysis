def f(x):
    y = 0
    while x > 0:
        if y == 1:
            x = y | (y + 1)
            x = x - y
        else:
            y = 1
            x = x - y
    return None