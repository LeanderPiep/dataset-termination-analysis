# label: t

FEATURE_ENABLED = True

def loop_condition(x):
    return x > 0

def assign_and_decrement(x, y):
    x = y
    y = y - 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x):
        x, y = assign_and_decrement(x, y)
    return None