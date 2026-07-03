# label: f

FEATURE_ENABLED = True

def should_enter_loop(c):
    return c >= 2

def should_continue(x, c):
    return x + c >= 0

def update_state(x, c):
    x = x - c
    c = c + 1
    return x, c

def main(c, x):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(c):
        while should_continue(x, c):
            x, c = update_state(x, c)
    return None