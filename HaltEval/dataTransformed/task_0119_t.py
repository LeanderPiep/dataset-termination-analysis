# label: t

FEATURE_ENABLED = True

def should_continue(x, y):
    return x - y > 0

def update_state(x, y, z):
    x = -x + y
    y = z
    z = z + 1
    return x, y, z

def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y):
        x, y, z = update_state(x, y, z)
    return None