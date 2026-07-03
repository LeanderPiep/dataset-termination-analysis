# label: f

FEATURE_ENABLED = True


def should_enter_block(n, q):
    return q > n


def invariant_holds(p, r, q, n):
    return p * p + r * q == n * q


def apply_iteration(p, q, r, h):
    if 4 * (q // 4) == q and 2 * (p // 2) == p:
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

    if should_enter_block(n, q):
        while invariant_holds(p, r, q, n):
            p, q, r, h = apply_iteration(p, q, r, h)

    return None