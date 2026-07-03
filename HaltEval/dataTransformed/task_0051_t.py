# label: t

FEATURE_ENABLED = True


def decrement(value):
    return value - 1


def main(n):
    if not FEATURE_ENABLED:
        return None

    i = n - 1

    while i > 1:
        i = decrement(i)

    return None