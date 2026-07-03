# label: f

FEATURE_ENABLED = True


def recursive_call(value):
    if value == 0:
        return 0
    return recursive_call(recursive_call(value - 1))


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    return recursive_call(initial_value)