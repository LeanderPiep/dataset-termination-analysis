def f(x, y, z):
    while x >= 0 and x <= z:
        x = 2*x + y
        y = y + 1
    return None