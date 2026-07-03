# label: t

FEATURE_ENABLED = True

def should_continue(x, y):
    return x + y > 0

def update_state(x, y):
    x = x - 1
    y = -2 * y
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y):
        x, y = update_state(x, y)
    return None