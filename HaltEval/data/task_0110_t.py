def f(a, b):
    while a >= 0:
        a = a + b
        if b >= 0:
            b = -b - 1
        else:
            b = -b
    return None