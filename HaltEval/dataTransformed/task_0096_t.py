# label: t

FEATURE_ENABLED = True

def should_continue(q):
    return q > 0

def apply_update(q, z):
    q = q + z - 1
    z = -z
    return q, z

def main(q, z):
    if not FEATURE_ENABLED:
        return None

    while should_continue(q):
        q, z = apply_update(q, z)
    return None