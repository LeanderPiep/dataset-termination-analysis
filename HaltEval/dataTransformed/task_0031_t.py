# label: t

FEATURE_ENABLED = True


def update_pair(q, p):
    if q < p:
        q -= 1
    else:
        if p < q:
            p -= 1
        else:
            return q, p, True
    return q, p, False


def main(initial_q, initial_p):
    if not FEATURE_ENABLED:
        return None

    q = initial_q
    p = initial_p

    while q > 0 and p > 0:
        q, p, should_break = update_pair(q, p)
        if should_break:
            break

    return None