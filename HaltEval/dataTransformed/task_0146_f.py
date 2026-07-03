# label: f

FEATURE_ENABLED = True

def should_continue(x, y):
    return x > 0 and y > 0

def update_state(x, y):
    x = 10 * y - 2 * x
    return x

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y):
        x = update_state(x, y)
    return None