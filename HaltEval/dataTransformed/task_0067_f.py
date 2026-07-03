# label: f

FEATURE_ENABLED = True


def update_state(x, y):
    x = -y
    y = y + 1
    return x, y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    while x < 10:
        x, y = update_state(x, y)

    return None