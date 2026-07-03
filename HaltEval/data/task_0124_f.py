def f(X, Y):
    v = 2 * Y - X
    y = 0
    x = 0
    c = 0

    while 2*Y*x - 2*X*y - X + 2*Y - v == 0:
        if v < 0:
            v = v + 2 * Y
        else:
            v = v + 2 * (Y - X)
            y += 1
        x += 1
        c += 1
    return None