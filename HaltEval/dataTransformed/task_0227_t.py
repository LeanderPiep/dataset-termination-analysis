# label: t

FEATURE_ENABLED = True


def should_continue(x, y, n):
    return x + y >= 0 and x <= n


def apply_iteration(x, y, z):
    x = 2 * x + y
    y = z
    z = z + 1
    return x, y, z


def main(x, y, z, n):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x, y, n):
        x, y, z = apply_iteration(x, y, z)

    return None