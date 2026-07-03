def f(x, y):
    z = 0
    i = x
    if y > 0 and x > 0:
        while i > 0:
            i = i - 1
            z = z + 1
        while i < y:
            i = i + 1
            z = z - 1
    return None