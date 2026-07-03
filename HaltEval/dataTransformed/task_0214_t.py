# label: f

FEATURE_ENABLED = True


def loop_condition(x, y, z):
    return x + y >= 0 and x <= z


def update_values(x, y):
    x = 2 * x + y
    y = y + 1
    return x, y


def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, y, z):
        x, y = update_values(x, y)

    return None