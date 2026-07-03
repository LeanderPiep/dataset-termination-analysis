# label: t

FEATURE_ENABLED = True


def update_state(x, y):
    x = 2 * x + y
    y += 1
    return x, y


def main(initial_x, initial_y, limit_value):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    while x >= 0 and x <= limit_value:
        x, y = update_state(x, y)

    return None