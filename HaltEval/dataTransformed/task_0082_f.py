# label: f

FEATURE_ENABLED = True


def update_y(y):
    return y - 1


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    if y >= 5:
        while x >= 0:
            y = update_y(y)

    return None