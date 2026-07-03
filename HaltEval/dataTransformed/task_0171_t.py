# label: t

FEATURE_ENABLED = True

def loop_condition(q):
    return q > 0

def update_values(q, a, b):
    olda = a
    q = q + a - 1
    a = 3 * olda - 4 * b
    b = 4 * olda + 3 * b
    return q, a, b

def main(q, a, b):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(q):
        q, a, b = update_values(q, a, b)
    return 0