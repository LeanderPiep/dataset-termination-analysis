def f(a):
    n = 0
    x = 0
    y = 1
    z = 6
    while x == n * n * n:
        n += 1
        x += y
        y += z
        z += 6
    return None