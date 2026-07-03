def f(z, k):
    x = 1
    y = 1
    c = 1
    while True:
        if 1 + x*z - x - z*y != 0:
            break
        c += 1
        x = x * z + 1
        y = y * z
    return None