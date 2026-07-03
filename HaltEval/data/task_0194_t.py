
def f(m, n, r):
    if not (p >= 0 and n >= 0 and r >= 0):
        return None
    if r > 0:
        return f(m, r-1, n)
    else:
        if n > 0:
            return f(r, n-1, m)
        else:
            return m
    return None
