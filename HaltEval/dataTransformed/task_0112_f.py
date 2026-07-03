# label: f

FEATURE_ENABLED = True

def should_continue(x):
    return x < 0

def update_state(x, y, z):
    x = x + z
    z = -2 * y
    y = y + 1
    return x, y, z

def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x, y, z = update_state(x, y, z)
    return None