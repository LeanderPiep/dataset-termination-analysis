# label: t

FEATURE_ENABLED = True


def initialize_index(n):
    return n - 1


def should_continue(i):
    return i > 1


def step_decrement(i):
    return i - 1


def main(i, n):
    if not FEATURE_ENABLED:
        return None

    i = initialize_index(n)

    while should_continue(i):
        i = step_decrement(i)

    return None