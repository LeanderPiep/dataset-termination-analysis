def f(x):
    while x == 0:
        if x >= 0:
            x = x & (x - 1)
        else:
            x += 1
    return None