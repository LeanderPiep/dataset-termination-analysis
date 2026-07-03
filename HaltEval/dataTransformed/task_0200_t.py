# label: t

FEATURE_ENABLED = True


def initialize_x(x_choice):
    return 1 if x_choice != 0 else -1


def loop_condition(y, z):
    return y < 100 and z < 100


def update_values(y, z, x):
    y = y + x
    z = z - x
    return y, z


def main(y, z, x_choice):
    if not FEATURE_ENABLED:
        return None

    x = initialize_x(x_choice)

    while loop_condition(y, z):
        y, z = update_values(y, z, x)

    return None