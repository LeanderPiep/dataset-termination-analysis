# label: f

FEATURE_ENABLED = True


def should_continue(x, y):
    return 4 * x - 5 * y > 0


def apply_transition(previous_x, y):
    next_x = 2 * previous_x + 4 * y
    next_y = 4 * previous_x
    return next_x, next_y


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    previous_x = x

    while should_continue(x, y):
        previous_x = x
        x, y = apply_transition(previous_x, y)

    return None