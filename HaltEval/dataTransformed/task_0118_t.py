# label: t

FEATURE_ENABLED = True

def should_enter_loop(x, y):
    return y > x

def should_continue(x):
    return x >= 0

def update_state(x, y):
    x = x - y
    return x

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(x, y):
        while should_continue(x):
            x = update_state(x, y)
    return None