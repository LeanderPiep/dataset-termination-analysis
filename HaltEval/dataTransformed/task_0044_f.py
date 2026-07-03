# label: f

FEATURE_ENABLED = True
MIN_INT = -2147483648


def update_negative(i):
    i = i + 2
    if i < 0:
        if i <= MIN_INT:
            return None, True
        i = -i
    return i, False


def update_positive(i):
    i = i - 2
    if i > 0:
        i = -i
    return i


def main(initial_i):
    if not FEATURE_ENABLED:
        return None

    i = initial_i

    while i != 0:
        if i < 0:
            i, should_stop = update_negative(i)
            if should_stop:
                return None
        else:
            i = update_positive(i)

    return None