def f(a, b):
    olda = a
    while a >= 7:
        olda = a
        a = b
        b = olda + 1
    return None