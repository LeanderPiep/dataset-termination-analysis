# label: f

FEATURE_ENABLED = True

def should_continue(x):
    return x < 5

def update_state(x, y):
    oldx = x
    x = oldx - y
    y = oldx + y
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    oldx = x
    while should_continue(x):
        x, y = update_state(x, y)
    return None