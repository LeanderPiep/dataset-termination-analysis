# label: f

FEATURE_ENABLED = True


def update_value(i):
    if i > 0:
        i -= 1
    if i < 0:
        i += 1
    return i


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    i = initial_value

    while -5 <= i <= 5:
        i = update_value(i)

    return None