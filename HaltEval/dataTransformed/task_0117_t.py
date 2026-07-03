# label: t

FEATURE_ENABLED = True

def should_continue(x, y):
    return x < y

def update_state(x, y, z):
    x = x + 1
    y = z
    return x, y

def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y):
        x, y = update_state(x, y, z)
    return None