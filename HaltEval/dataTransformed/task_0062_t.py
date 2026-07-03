# label: t

FEATURE_ENABLED = True


def update_state(x, y, z):
    x = x + y
    y = z
    z = -z - 1
    return x, y, z


def main(initial_x, initial_y, initial_z):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y
    z = initial_z

    while x >= 0:
        x, y, z = update_state(x, y, z)

    return None