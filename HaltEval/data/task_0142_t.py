def f(x, c):
    if c >= 2:
        while x + c >= 0:
            x = x - c
            c = c + 1
    return None