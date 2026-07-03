# label: f

FEATURE_ENABLED = True


def should_continue(n, y):
    return y == 3 * n * n + 3 * n + 1


def apply_iteration(n, x, y, z):
    n = n + 1
    x = x + y
    y = y + z
    z = z + 6
    return n, x, y, z


def main(a):
    if not FEATURE_ENABLED:
        return None

    n = 0
    x = 0
    y = 1
    z = 6

    while should_continue(n, y):
        n, x, y, z = apply_iteration(n, x, y, z)

    return None