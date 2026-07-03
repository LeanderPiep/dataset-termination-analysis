# label: t

FEATURE_ENABLED = True


def should_continue(x):
    return x > 0


def apply_update(x, y):
    x = x + y
    y = y - 1
    return x, y


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x, y = apply_update(x, y)

    return None