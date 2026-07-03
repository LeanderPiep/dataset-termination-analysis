# label: f

FEATURE_ENABLED = True


def helper(value):
    if value <= 0:
        return 0
    return main(value - 1) + main(value - 2)


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    if initial_value <= 0:
        return 0

    return helper(initial_value) + helper(initial_value + 1)