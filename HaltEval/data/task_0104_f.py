def f(i, j):
    s = 1
    t = 1
    while t*t - 4*s + 2*t + 1 + i >= 0:
        t = t + 2
        s = s + t
        i = i + j
        j = j + 1
    return None