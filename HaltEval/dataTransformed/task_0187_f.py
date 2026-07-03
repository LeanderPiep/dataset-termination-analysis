# label: f

FEATURE_ENABLED = True

def loop_condition(x, y):
    return x < y

def update_values(x, y):
    x = x + y
    y = -2 * y
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, y):
        x, y = update_values(x, y)
    return None