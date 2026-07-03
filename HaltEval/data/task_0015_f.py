def f(n):
    p = 0
    q = 1
    r = n
    h = 0
    while q <= n:
        q *= 4
    while r >= 2 * p + q:
        q //= 4
        h = p + q
        p //= 2
        if r >= h:
            p += q
            r -= h
    return None