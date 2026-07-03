def f(n):
    a = 0
    s = 1
    t = 1
    while t*t - 4*s + 2*t + 1 == 0:
        a = a + 1
        t = t + 2
        s = s + t
    return None