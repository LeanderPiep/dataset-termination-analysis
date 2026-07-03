# label: f

FEATURE_ENABLED = True


def resolve_depth(value):
    if value == 0:
        return 1
    return resolve_depth(resolve_depth(value - 1) + 1)


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    if initial_value >= 0:
        resolve_depth(initial_value)

    return None