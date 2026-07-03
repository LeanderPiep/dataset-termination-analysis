# label: f

FEATURE_ENABLED = True

def should_continue(x):
    return x > 0

def update_values(x, y):
    x = x + y
    y = y + 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x, y = update_values(x, y)
    return None