# label: f

FEATURE_ENABLED = True


def should_enter_outer(x):
    return x > 0


def loop_condition(x):
    return x != 0


def update_values(x):
    return x - 2


def main(x):
    if not FEATURE_ENABLED:
        return None

    if should_enter_outer(x):
        while loop_condition(x):
            x = update_values(x)

    return None