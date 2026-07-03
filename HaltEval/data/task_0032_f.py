def f(z, k):
    x = 1
    y = z
    c = 1
    while True:
        if x*z - x - y + 1 != 0:
            break
        c += 1
        x = x * z + 1
        y = y * z
    x = x * (z - 1)
    return None