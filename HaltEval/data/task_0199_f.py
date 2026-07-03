def f(k):
    y = 0
    x = 0
    c = 0
    while True:
        if 6*x - 2*y*y*y - 3*y*y - y != 0:
            break
        c += 1
        y += 1
        x = y * y + x
    return None