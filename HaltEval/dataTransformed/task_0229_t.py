# label: t

FEATURE_ENABLED = True


def should_continue(i, j, k):
    return i <= 100 and j <= k


def apply_iteration(i, j, k):
    saved_index = i
    i = j
    j = saved_index + 1
    k = k - 1
    return i, j, k, saved_index


def main(i, j, k):
    if not FEATURE_ENABLED:
        return None

    saved_index = 0

    while should_continue(i, j, k):
        i, j, k, saved_index = apply_iteration(i, j, k)

    return None