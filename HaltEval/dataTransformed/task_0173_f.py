# label: f

FEATURE_ENABLED = True

def loop_condition(x):
    return x < 5

def update_values(x, y):
    oldx = x
    x = oldx - y
    y = oldx + y
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x):
        x, y = update_values(x, y)
    return None