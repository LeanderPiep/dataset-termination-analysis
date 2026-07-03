# label: f

FEATURE_ENABLED = True

def should_enter_loop(x, y):
    return x + y >= 0

def loop_condition(x):
    return x > 0

def update_values(x, y):
    x = x + x + y
    y = y + 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(x, y):
        while loop_condition(x):
            x, y = update_values(x, y)
    return None