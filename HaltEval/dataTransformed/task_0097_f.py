# label: f

FEATURE_ENABLED = True

def should_continue(x):
    return x < 10

def update_state(x, y):
    x = -y
    y = y + 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x, y = update_state(x, y)
    return None