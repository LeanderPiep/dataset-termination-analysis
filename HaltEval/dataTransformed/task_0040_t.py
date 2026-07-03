# label: t

FEATURE_ENABLED = True


def update_state(x, y):
    x = x - y
    y = y + 1
    return x, y


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    x = initial_value
    y = 1

    while x > 0:
        x, y = update_state(x, y)

    return None