def f(x, y, z):
    while x >= 0 and x + y >= 0:
        x = x + y + z
        y = -z - 1
    return None