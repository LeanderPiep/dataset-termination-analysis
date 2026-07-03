# label: f

FEATURE_ENABLED = True


def should_enter_block(n, q):
    return q > n


def loop_condition(h, n, p, q, r):
    return (
        h * h * n
        - 4 * h * n * p
        + 4 * (n * n) * q
        - n * q * q
        - h * h * r
        + 4 * h * p * r
        - 8 * n * q * r
        + q * q * r
        + 4 * q * r * r
        == 0
    )


def update_values(p, q, r, h):
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
        while loop_condition(h, n, p, q, r):
            p, q, r, h = update_values(p, q, r, h)

    return None