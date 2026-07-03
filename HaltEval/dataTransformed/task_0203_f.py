# label: f

FEATURE_ENABLED = True


def should_process(n, q):
    return q > n


def loop_condition(r, p, q):
    return r < 2 * p + q


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

    if should_process(n, q):
        while loop_condition(r, p, q):
            p, q, r, h = update_values(p, q, r, h)

    return None