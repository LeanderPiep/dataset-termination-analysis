# label: t

FEATURE_ENABLED = True


def should_enter_loop(x, y):
    return x < y


def update_values(x, y, z):
    x += 1
    y = z
    return x, y


def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    while should_enter_loop(x, y):
        x, y = update_values(x, y, z)

    return None