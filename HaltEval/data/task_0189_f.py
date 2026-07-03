def f(s, a):
    if s >= 8192:
        return None
    if a <= 2:
        return None
    n = s*s
    d = a
    r = n % d
    t = 0
    k = n % (d - 2)
    q = 4 * (n / (d - 2) - n / d)
    while True:
        if d * k - d * t - a * k + a * t != 0:
            break
        if 2 * r + q < k:
            t = r
            r = 2 * r - k + q + d + 2
            k = t
            q = q + 4
            d = d + 2
        elif 2 * r + q >= k and 2 * r + q < d + k + 2:
            t = r
            r = 2 * r - k + q
            k = t
            d = d + 2
        elif 2 * r + q >= k and 2 * r + q >= d + k + 2 and 2 * r + q < 2 * d + k + 4:
            t = r
            r = 2 * r - k + q - d - 2
            k = t
            q = q - 4
            d = d + 2
        else:
            t = r
            r = 2 * r - k + q - 2 * d - 4
            k = t
            q = q - 8
            d = d + 2
    return None