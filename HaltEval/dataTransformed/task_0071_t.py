# label: t

FEATURE_ENABLED = True


def grow_until_limit(y, x):
    while y < x:
        y = 2 * y
    return y


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = initial_x

    while x >= 0:
        y = 1
        y = grow_until_limit(y, x)
        x -= 1

    return None