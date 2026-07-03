# label: f

FEATURE_ENABLED = True


def update_state(x, y):
    x = x + y
    y = -2 * y
    return x, y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    while x < y:
        x, y = update_state(x, y)

    return None