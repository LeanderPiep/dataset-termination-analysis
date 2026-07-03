# label: t

FEATURE_ENABLED = True


def outer_loop_condition(x):
    return x >= 0


def inner_loop_condition(y, x):
    return y < x


def update_inner(y):
    return y + 1


def update_outer(x):
    return x - 1


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while outer_loop_condition(x):
        y = 1
        while inner_loop_condition(y, x):
            y = update_inner(y)
        x = update_outer(x)

    return None