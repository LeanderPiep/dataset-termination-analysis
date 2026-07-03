# label: t

FEATURE_ENABLED = True

def loop_condition(x):
    return x >= 0

def update_values(x, y):
    x = x + y
    y = (-2) * y - 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x):
        x, y = update_values(x, y)
    return None