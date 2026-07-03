def f(x, y, z, i):
    while x < y:
        i = i + 1
        if z > x:
            x = x + 1
        else:
            z = z + 1
    return None