# label: t

FEATURE_ENABLED = True


def update_state(q, a, b):
    q = q + a - 1
    previous_a = a
    a = 3 * previous_a - 4 * b
    b = 4 * previous_a + 3 * b
    return q, a, b


def main(a, b, q):
    if not FEATURE_ENABLED:
        return None

    while q > 0:
        q, a, b = update_state(q, a, b)

    return None