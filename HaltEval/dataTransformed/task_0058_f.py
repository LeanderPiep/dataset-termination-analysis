# label: f

FEATURE_ENABLED = True


def update_value(x, y):
    return x + y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    while x > 0:
        x = update_value(x, y)

    return None