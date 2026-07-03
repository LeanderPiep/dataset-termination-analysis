# label: t

FEATURE_ENABLED = True

def loop_condition(i, j, k):
    return i <= 100 and j <= k

def update_values(i, j, k, tmp):
    tmp, i, j, k = i, j, tmp + 1, k - 1
    return i, j, k, tmp

def main(i, j, k, tmp):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(i, j, k):
        i, j, k, tmp = update_values(i, j, k, tmp)
    return None