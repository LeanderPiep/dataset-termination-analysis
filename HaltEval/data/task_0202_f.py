def f(a, b):
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