# label: f

FEATURE_ENABLED = True


def should_continue(x, y):
    return x < y


def apply_iteration(x, y):
    x = x + y
    y = y // 2
    return x, y


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y):
        x, y = apply_iteration(x, y)

    return None