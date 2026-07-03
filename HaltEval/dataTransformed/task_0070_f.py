# label: f

FEATURE_ENABLED = True


def update_state(i, j):
    if i < j:
        temp = i
        i = j
        j = temp
    else:
        if i > j:
            j = i
        else:
            i = i - 1
    return i, j


def main(initial_i, initial_j):
    if not FEATURE_ENABLED:
        return None

    i = initial_i
    j = initial_j
    t = 0  # kept for realism, not needed

    while i > 0 and j > 0:
        i, j = update_state(i, j)

    return None