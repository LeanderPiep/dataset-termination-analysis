# label: f

FEATURE_ENABLED = True

def loop_condition(x, y):
    return (y * y) - 2 * x + y == 0

def update_values(c, x, y):
    c = c + 1
    y = y + 1
    x = y + x
    return c, x, y

def main(k):
    if not FEATURE_ENABLED:
        return None

    y = 0
    x = 0
    c = 0

    while loop_condition(x, y):
        c, x, y = update_values(c, x, y)
    return None