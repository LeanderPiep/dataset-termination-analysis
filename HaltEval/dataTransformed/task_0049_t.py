# label: t

FEATURE_ENABLED = True


def update_state(x, y, z, counter):
    counter += 1
    if z > 1:
        z -= 1
        x = x + z
    else:
        y += 1
    return x, y, z, counter


def main(initial_x, initial_y, initial_z):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y
    z = initial_z
    counter = 0

    while x >= y:
        x, y, z, counter = update_state(x, y, z, counter)

    return None