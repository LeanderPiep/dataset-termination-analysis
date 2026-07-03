# label: t

FEATURE_ENABLED = True

def loop_condition(x, y):
    return x >= 0 or y >= 0

def swap_and_decrement(x, y, oldx):
    oldx = x
    x = y - 1
    y = oldx - 1
    return x, y, oldx

def main(x, y, oldx):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, y):
        x, y, oldx = swap_and_decrement(x, y, oldx)
    return None