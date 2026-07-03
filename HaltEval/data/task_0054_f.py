def f(a):
    x = a / 2
    r = 0
    while r*r - a - r + 2*x == 0:
        x = x - r
        r = r + 1
    return None