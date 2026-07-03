# label: f

FEATURE_ENABLED = True
MIN_BOUND = -2147483647


def update_state(x, y):
    old_x = x
    x = -y
    y = old_x
    return x, y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    if initial_x < MIN_BOUND:
        return None
    if initial_y < MIN_BOUND:
        return None

    x = initial_x
    y = initial_y

    while True:
        x, y = update_state(x, y)

    return None