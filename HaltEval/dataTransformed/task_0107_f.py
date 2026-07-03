# label: f

FEATURE_ENABLED = True

def should_continue(x):
    return x > 0

def update_state(x, y):
    x = x + y
    y = -2 * y
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x, y = update_state(x, y)
    return None