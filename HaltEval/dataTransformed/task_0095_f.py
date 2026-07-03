# label: f

FEATURE_ENABLED = True

def should_enter_loop(n, p, q, r):
    return q > n and (p * p - n * q + q * r == 0)

def can_reduce_state(p, q):
    return 4 * (q // 4) == q and 2 * (p // 2) == p

def update_state(p, q, r, h):
    q = q // 4
    h = p + q
    p = p // 2
    if r >= h:
        p = p + q
        r = r - h
    return p, q, r, h

def main(n):
    if not FEATURE_ENABLED:
        return None

    p = 0
    q = 1
    r = n
    h = 0

    if q > n:
        while p * p - n * q + q * r == 0:
            if can_reduce_state(p, q):
                p, q, r, h = update_state(p, q, r, h)
    return None