def f(k):
    y = 0
    x = 0
    c = 0
    while True:
        if (y * y) - 2 * x + y != 0:
            break
        c += 1
        y += 1
        x = y + x
    return None