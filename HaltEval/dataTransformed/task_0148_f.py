# label: f

FEATURE_ENABLED = True

def should_continue(i, j):
    return i != 0 and j != 0

def swap_values(i, j, t):
    t = i
    i = j
    j = t
    return i, j, t

def main(i, j):
    if not FEATURE_ENABLED:
        return None

    t = 0
    while should_continue(i, j):
        i, j, t = swap_values(i, j, t)
    return None