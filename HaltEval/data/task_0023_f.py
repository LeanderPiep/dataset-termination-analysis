def f(x, y, z):
    while x > 0:
        x = x + y
        y = y + z
        z = z + x
    return None