def f(x, y, z, n):
    while x + y >= 0 and x <= n:
        x = 2 * x + y
        y = z
        z = z + 1
    return None