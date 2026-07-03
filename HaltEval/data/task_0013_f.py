def f(z, a, k):
    x = a
    y = 1
    c = 1

    while True:
        if z*x - x + a - a*z*y != 0:
            break

        c += 1
        x = x * z + a
        y = y * z

    return x