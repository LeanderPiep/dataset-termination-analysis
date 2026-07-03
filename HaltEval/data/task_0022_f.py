def f(a):
    n = 0
    x = 0
    y = 1
    z = 6
    while z <= 6 * n + 6:
        n = n + 1
        x = x + y
        y = y + z
        z = z + 6
    return None