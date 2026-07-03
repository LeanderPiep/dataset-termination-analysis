# label: t

FEATURE_ENABLED = True


def update_q(q, y):
    if y > 0:
        q = q - y - 1
    else:
        q = q + y - 1
    return q


def main(initial_q, y):
    if not FEATURE_ENABLED:
        return None

    q = initial_q

    while q > 0:
        q = update_q(q, y)

    return None