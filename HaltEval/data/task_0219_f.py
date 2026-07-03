def f(x, y):
    oldx = x
    while 4*x - 5*y > 0:
        oldx = x
        x = 2*oldx + 4*y
        y = 4*oldx
    return None