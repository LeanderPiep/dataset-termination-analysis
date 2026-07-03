# label: t

FEATURE_ENABLED = True

def should_continue(x):
    return x >= 0

def update_state(x):
    x = -2 * x + 10
    return x

def main(x):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x = update_state(x)
    return None