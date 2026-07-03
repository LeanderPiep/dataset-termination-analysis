# label: t

FEATURE_ENABLED = True


def update_value(value):
    return -2 * value + 10


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    value = initial_value

    while value > 0:
        value = update_value(value)

    return None