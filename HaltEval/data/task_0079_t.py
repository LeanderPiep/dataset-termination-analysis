def f(y, z, x):
    x = 1 if x else -1
    while y < 100 and z < 100:
        y = y + x
        z = z - x
    return None