def f(a, b):
    if a < 1 or b < 1 or a > 65535 or b > 65535:
        return None

    x = a
    y = b
    u = b
    v = 0

    while True:
        if x*u + y*v != a*b:
            break

        while True:
            if x*u + y*v != a*b:
                break
            x = x - y
            v = v + u

        while True:
            if x*u + y*v != a*b:
                break
            y = y - x
            u = u + v

    return None