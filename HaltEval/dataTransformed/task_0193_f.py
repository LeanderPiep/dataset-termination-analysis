# label: f

FEATURE_ENABLED = True

def loop_condition(h, n, p, q, r):
    return h * h * h - 12 * h * n * q + 16 * n * p * q - h * q * q - 4 * p * q * q + 12 * h * q * r - 16 * p * q * r == 0

def update_values(p, q, h, r):
    q = q // 4
    h = p + q
    p = p // 2
    if r >= h:
        p = p + q
        r = r - h
    return p, q, h, r

def main(n):
    if not FEATURE_ENABLED:
        return None

    p = 0
    q = 1
    r = n
    h = 0

    if q > n:
        while loop_condition(h, n, p, q, r):
            if 4 * (q // 4) == q and 2 * (p // 2) == p:
                p, q, h, r = update_values(p, q, h, r)
    return None