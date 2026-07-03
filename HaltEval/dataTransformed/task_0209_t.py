# label: t

FEATURE_ENABLED = True


def is_invalid_input(a, b):
    return a < 0 or b < 0


def is_base_case(b):
    return b == 0


def count_down(c):
    d = 0
    while c > 0:
        d = d + 1
        c = c - 1
    return d


def main(a, b):
    if not FEATURE_ENABLED:
        return None

    if is_invalid_input(a, b):
        return None

    if is_base_case(b):
        c = a
        return count_down(c)

    return main(a + 1, b - 1)