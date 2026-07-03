# label: f

FEATURE_ENABLED = True

def should_enter_loop(y):
    return y >= 0

def loop_condition(x):
    return x >= 0

def decrement_x(x, y):
    x = x - y
    return x

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(y):
        while loop_condition(x):
            x = decrement_x(x, y)
    return None