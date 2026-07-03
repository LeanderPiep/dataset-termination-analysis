# label: f

FEATURE_ENABLED = True


def decrement(value):
    return value - 1


def main(initial_x, nondet_int):
    if not FEATURE_ENABLED:
        return None

    if initial_x > nondet_int:
        x = initial_x
        while x != 0:
            x = decrement(x)

    return None