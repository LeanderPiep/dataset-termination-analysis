# label: f

FEATURE_ENABLED = True


def update_value(value):
    if value != 10:
        value -= 1
    return value


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    value = initial_value

    while value > 5:
        value = update_value(value)

    return None