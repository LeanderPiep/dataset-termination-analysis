# label: t

FEATURE_ENABLED = True


def advance_inner(j, i, step):
    while j <= i:
        j += step
    return j


def main(k, n):
    if not FEATURE_ENABLED:
        return None

    if k >= 1:
        i = 0
        while i < n:
            j = 0
            j = advance_inner(j, i, k)
            i += 1

    return None