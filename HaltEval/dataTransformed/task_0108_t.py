# label: t

FEATURE_ENABLED = True

def should_continue(i, j, k):
    return i <= 100 and j <= k

def update_state(i, j, k):
    ell = i
    i = j
    j = ell + 1
    k = k - 1
    return i, j, k

def main(i, j, k):
    if not FEATURE_ENABLED:
        return None

    while should_continue(i, j, k):
        i, j, k = update_state(i, j, k)
    return None