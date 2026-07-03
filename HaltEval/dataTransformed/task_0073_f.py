# label: f

FEATURE_ENABLED = True


def update_value(i):
    if i < 20:
        i -= 1
    if i > 10:
        i += 1
    if 30 <= i <= 40:
        i -= 1
    return i


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    i = initial_value

    while i > 0 and i < 50:
        i = update_value(i)

    return None