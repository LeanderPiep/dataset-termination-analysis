def f(x):
    y = 2
    while x >= 0:
        x = x - y
        y = (y + 1) // 2
    return None