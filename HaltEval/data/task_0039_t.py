def f(x, a, b):
    if a != b:
        return None
    while x >= 0:
        x = x + a - b - 1
    return None