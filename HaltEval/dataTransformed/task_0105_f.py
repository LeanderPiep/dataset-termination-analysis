# label: f

FEATURE_ENABLED = True

def should_enter_loop(c):
    return c == 0

def should_continue(x):
    return x >= 0

def update_state(x, c):
    x = x + c
    return x

def main(x, c):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(c):
        while should_continue(x):
            x = update_state(x, c)
    return None