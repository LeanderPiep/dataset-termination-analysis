# label: t

FEATURE_ENABLED = True

def should_initialize(n, m):
    return m > 0 and n > m

def should_continue(i, n):
    return i < n

def update_state(i, j, m):
    if j < m:
        j = j + 1
    else:
        j = 0
        i = i + 1
    return i, j

def main(n, m):
    if not FEATURE_ENABLED:
        return None

    if should_initialize(n, m):
        i = 0
        j = 0
        while should_continue(i, n):
            i, j = update_state(i, j, m)
    return None