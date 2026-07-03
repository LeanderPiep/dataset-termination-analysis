# label: t

FEATURE_ENABLED = True

def should_continue(q):
    return q > 0

def update_state(q, a, b):
    olda = a
    q = q + a - 1
    a = 3 * olda - 4 * b
    b = 4 * olda + 3 * b
    return q, a, b

def main(q, a, b):
    if not FEATURE_ENABLED:
        return None

    olda = a
    while should_continue(q):
        q, a, b = update_state(q, a, b)
        olda = a
    return None