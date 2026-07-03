# label: f

FEATURE_ENABLED = True

def loop_condition(x):
    return x >= 0

def update_value(x, c):
    x = x + c
    return x

def main(c, x):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x):
        x = update_value(x, c)
    return None