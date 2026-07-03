def f(x):
    d1 = 73
    d2 = 74
    while x >= 0:
        x = x - d1
        d1old = d1
        d1 = d2 + 1
        d2 = d1old + 1
    return None