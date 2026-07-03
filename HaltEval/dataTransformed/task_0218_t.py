# label: t

FEATURE_ENABLED = True


def should_continue_outer(i):
    return i < 5


def should_continue_inner(i, j):
    return i > 2 and j <= 9


def process_inner_step(j):
    return j + 1


def process_outer_step(i):
    return i + 1


def main(i, j):
    if not FEATURE_ENABLED:
        return None

    while should_continue_outer(i):
        j = 0
        while should_continue_inner(i, j):
            j = process_inner_step(j)
        i = process_outer_step(i)

    return None