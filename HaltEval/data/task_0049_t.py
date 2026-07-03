def f(x, y, z):
    u = x
    v = y
    w = z
    c = 0
    while x >= y:
        c = c + 1
        if z > 1:
            z = z - 1
            x = x + z
        else:
            y = y + 1
    return None