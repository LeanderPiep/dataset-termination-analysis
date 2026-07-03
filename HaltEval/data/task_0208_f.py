def f(a, b):
    if a < 1 or b < 1 or a > 65535 or b > 65535:
        return None

    x = a
    y = b
    u = b
    v = a

    while True:
        if x*u + y*v != 2*a*b:
            break

        if x > y:
            x = x - y
            v = v + u
        else:
            y = y - x
            u = u + v

    return None