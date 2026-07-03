# label: t

FEATURE_ENABLED = True


def update_value(value, offset_a, offset_b):
    return value + offset_a - offset_b - 1


def main(initial_value, offset_a, offset_b):
    if not FEATURE_ENABLED:
        return None

    if offset_a != offset_b:
        return None

    value = initial_value
    while value >= 0:
        value = update_value(value, offset_a, offset_b)

    return None