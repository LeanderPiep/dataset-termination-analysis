def f(n):
    p = 0
    q = 1
    r = n
    h = 0

    if q > n:
        while h * h * h - 12 * h * n * q + 16 * n * p * q - h * q * q - 4 * p * q * q + 12 * h * q * r - 16 * p * q * r == 0:
            if 4 * (q // 4) == q and 2 * (p // 2) == p:
                q = q // 4
                h = p + q
                p = p // 2
                if r >= h:
                    p = p + q
                    r = r - h
    return None