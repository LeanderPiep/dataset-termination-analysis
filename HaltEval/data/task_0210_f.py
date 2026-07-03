def f(k):
    y = 0
    x = 0
    c = 0

    while True:
        if not (4*x - y*y*y*y - 2*y*y*y - y*y == 0):
            break

        c = c + 1
        y = y + 1
        x = y * y * y + x

    return None