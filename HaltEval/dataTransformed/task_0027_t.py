# label: t

FEATURE_ENABLED = True


def update_pair(prev_x, prev_y):
    new_x = prev_y - 1
    new_y = prev_x - 1
    return new_x, new_y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y

    while x >= 0 or y >= 0:
        x, y = update_pair(x, y)

    return None