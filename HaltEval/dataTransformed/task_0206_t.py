# label: t

FEATURE_ENABLED = True


def loop_condition(x):
    return x >= 0


def should_enter_inner_loop(y, x):
    return y < x


def update_values(x, y):
    y = 1
    while should_enter_inner_loop(y, x):
        y = 2 * y
    x = x - 1
    return x, y


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x):
        x, y = update_values(x, y)

    return None