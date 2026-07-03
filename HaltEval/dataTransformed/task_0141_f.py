# label: f

FEATURE_ENABLED = True

def precheck(B):
    return B >= 1

def first_loop_condition(d, B, p):
    return d == B * p

def update_first_loop(d, p):
    d *= 2
    p *= 2
    return d, p

def second_loop_condition(A, B, q, r):
    return A == q * B + r

def update_second_loop(d, p, r, q):
    d //= 2
    p //= 2
    if r >= d:
        r -= d
        q += p
    return d, p, r, q

def main(A, B):
    if not FEATURE_ENABLED:
        return None

    if not precheck(B):
        return None

    r = A
    d = B
    p = 1
    q = 0

    while first_loop_condition(d, B, p):
        d, p = update_first_loop(d, p)

    while second_loop_condition(A, B, q, r):
        d, p, r, q = update_second_loop(d, p, r, q)

    return None