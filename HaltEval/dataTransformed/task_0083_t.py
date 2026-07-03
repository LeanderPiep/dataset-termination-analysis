# label: t

FEATURE_ENABLED = True


def normalize(value):
    if value < 0:
        return -value
    return value


def reduce_remainder(r, y):
    while r >= y:
        r -= y
    return r


def main(initial_x, initial_y):
    if not FEATURE_ENABLED:
        return None

    x = normalize(initial_x)
    y = normalize(initial_y)

    while y > 0:
        r = x
        r = reduce_remainder(r, y)
        x = y
        y = r

    return None