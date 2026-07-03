def f(n):
    p = 0
    q = 1
    r = n
    h = 0

    if q > n:
        while p * p - n * q + q * r == 0:
            if 4 * (q // 4) == q and 2 * (p // 2) == p:
                q = q // 4
                h = p + q
                p = p // 2
                if r >= h:
                    p = p + q
                    r = r - h
    return None