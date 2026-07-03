def f(x, y, z):
    y = 100
    z = 1
    while x >= 0:
        x = x - y
        y = y - z
        z = -z
    return None