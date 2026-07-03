# label: t

FEATURE_ENABLED = True


def should_run(a, b):
    return a == b


def should_continue(x, y):
    return x >= 0 or y >= 0


def apply_iteration(a, b, x, y):
    x = x + a - b - 1
    y = y + b - a - 1
    return x, y


def main(a, b, x, y):
    if not FEATURE_ENABLED:
        return None

    if should_run(a, b):
        while should_continue(x, y):
            x, y = apply_iteration(a, b, x, y)

    return None