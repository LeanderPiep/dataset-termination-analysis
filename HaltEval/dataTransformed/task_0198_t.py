# label: t

FEATURE_ENABLED = True

def loop_condition(x):
    return x >= 0

def update_values(x, y):
    x = x - y
    y = (y + 1) // 2
    return x, y

def main(x):
    if not FEATURE_ENABLED:
        return None

    y = 2
    while loop_condition(x):
        x, y = update_values(x, y)
    return None