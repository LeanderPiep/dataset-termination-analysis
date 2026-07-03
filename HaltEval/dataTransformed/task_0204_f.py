# label: f

FEATURE_ENABLED = True


def should_enter_outer(y):
    return y < 1


def loop_condition(x):
    return x >= 0


def update_values(x, y):
    x = x - y
    return x


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if should_enter_outer(y):
        while loop_condition(x):
            x = update_values(x, y)

    return None