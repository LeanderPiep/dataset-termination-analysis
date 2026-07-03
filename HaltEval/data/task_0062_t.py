def f(x, y, z):
    while x >= 0:
        x = x + y
        y = z
        z = -z - 1
    return None