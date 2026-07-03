# label: t

FEATURE_ENABLED = True


def should_continue(x, y):
    return x > 0 and x < y


def apply_growth(x, y):
    x = 2 * x
    y = y + 1
    return x, y


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y):
        x, y = apply_growth(x, y)

    return None