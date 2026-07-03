# label: t

FEATURE_ENABLED = True


def update_state(x, z, counter):
    counter += 1
    if z > x:
        x += 1
    else:
        z += 1
    return x, z, counter


def main(initial_x, initial_y, initial_z, initial_i):
    if not FEATURE_ENABLED:
        return None

    x = initial_x
    y = initial_y
    z = initial_z
    counter = initial_i

    while x < y:
        x, z, counter = update_state(x, z, counter)

    return None