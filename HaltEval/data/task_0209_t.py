
def f(a, b):
    if a < 0 or b < 0:
        return None
    if b == 0:
        c = a
        d = 0
        while c > 0:
            d = d + 1
            c = c - 1
        return d
    else:
        return f(a + 1, b - 1)
