# label: f

FEATURE_ENABLED = True


def should_enter_loop(x):
    return x > 1


def update_values(x):
    return 2 * x


def main(x):
    if not FEATURE_ENABLED:
        return None

    while should_enter_loop(x):
        x = update_values(x)

    return None