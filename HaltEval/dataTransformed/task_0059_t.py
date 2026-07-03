# label: t

FEATURE_ENABLED = True


def update_state(x, y):
    x = x + y - 5
    y = -2 * y
    return x, y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    while x > 0:
        x, y = update_state(x, y)

    return None