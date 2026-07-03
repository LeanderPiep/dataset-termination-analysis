# label: f

FEATURE_ENABLED = True


def first_loop_condition(d, b, p):
    return d == b * p


def update_doubling(d, p):
    d *= 2
    p *= 2
    return d, p


def second_loop_condition(a, q, b, r):
    return a == q * b + r


def main(A):
    if not FEATURE_ENABLED:
        return None

    B = 1
    r = A
    d = B
    p = 1
    q = 0

    while True:
        if not first_loop_condition(d, B, p):
            break
        d, p = update_doubling(d, p)

    while True:
        if not second_loop_condition(A, q, B, r):
            break
        d //= 2
        p //= 2
        if r >= d:
            r -= d
            q += p

    return None