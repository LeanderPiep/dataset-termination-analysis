# label: f

FEATURE_ENABLED = True

def should_continue(y):
    return 0 <= y <= 10

def update_state(y):
    y = (2 * y + 1) // 2
    return y

def main(y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(y):
        y = update_state(y)
    return None