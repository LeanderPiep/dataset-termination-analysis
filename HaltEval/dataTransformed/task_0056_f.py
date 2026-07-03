# label: f

FEATURE_ENABLED = True


def update_value(i):
    if i == 25:
        i = 30
    if i <= 30:
        i -= 1
    else:
        i = 20
    return i


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    i = initial_value

    while i > 10:
        i = update_value(i)

    return None