# label: f

FEATURE_ENABLED = True


def update_state(counter, x, y, z):
    counter += 1
    x = x + y
    y = y + z
    z = z + 6
    return counter, x, y, z


def condition_holds(x, y, z):
    return y * z - 18 * x - 12 * y + 2 * z - 6 == 0


def main(input_value):
    if not FEATURE_ENABLED:
        return None

    counter = 0
    x = 0
    y = 1
    z = 6

    while condition_holds(x, y, z):
        counter, x, y, z = update_state(counter, x, y, z)

    return None