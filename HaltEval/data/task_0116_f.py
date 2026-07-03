def f(k):
    y = 0
    x = 0
    c = 0
    while True:
        if 6*y**5 + 15*y**4 + 10*y**3 - 30*x - y != 0:
            break
        c += 1
        y += 1
        x = y**4 + x
    return None