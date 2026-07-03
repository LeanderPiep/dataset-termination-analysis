# label: t

FEATURE_ENABLED = True

def should_continue(x, y):
    return x >= y

def decrement(x):
    return x - 1

def main(x):
    if not FEATURE_ENABLED:
        return None

    y = 23
    while should_continue(x, y):
        x = decrement(x)
    return None