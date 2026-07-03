def f(x, y, z):
    while x < 0:
        x = x + z
        z = -2*y
        y = y + 1
    return None