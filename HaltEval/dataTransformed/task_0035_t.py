# label: t

FEATURE_ENABLED = True


def update_index(i, threshold):
    if i < threshold:
        i -= 1
    else:
        i -= threshold
    return i


def main(n, m):
    if not FEATURE_ENABLED:
        return None

    if m > 0 and n > m:
        i = n
        while i > 0:
            i = update_index(i, m)

    return None