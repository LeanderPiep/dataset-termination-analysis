# label: t

FEATURE_ENABLED = True

def loop_condition(x, n):
    return 0 < x < n

def update_values(x, y):
    x = -x + y - 5
    y = 2 * y
    return x, y

def main(x, y, n):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, n):
        x, y = update_values(x, y)
    return None