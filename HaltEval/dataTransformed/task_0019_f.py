# label: f

FEATURE_ENABLED = True


def update_remaining(value, step):
    return value - step


def main(initial_value, step):
    if not FEATURE_ENABLED:
        return None

    if step <= initial_value:
        value = initial_value
        while value >= 0:
            value = update_remaining(value, step)

    return None