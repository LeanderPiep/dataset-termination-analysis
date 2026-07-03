# label: f

FEATURE_ENABLED = True

def should_continue(s, t, i):
    return t * t - 4 * s + 2 * t + 1 + i >= 0

def update_state(s, t, i, j):
    t = t + 2
    s = s + t
    i = i + j
    j = j + 1
    return s, t, i, j

def main(i, j):
    if not FEATURE_ENABLED:
        return None

    s = 1
    t = 1
    while should_continue(s, t, i):
        s, t, i, j = update_state(s, t, i, j)
    return None