# label: f

FEATURE_ENABLED = True

def should_exit_early(x1, x2):
    return x1 < 0 or x2 == 0

def invariant_holds(y1, y2, y3, x1, x2):
    return y1 * x2 + y2 + y3 == x1

def advance_state(y1, y2, y3, x2):
    if y2 + 1 == x2:
        y1 = y1 + 1
        y2 = 0
        y3 = y3 - 1
    else:
        y2 = y2 + 1
        y3 = y3 - 1
    return y1, y2, y3

def main(x1, x2):
    if not FEATURE_ENABLED:
        return None

    if should_exit_early(x1, x2):
        return None

    y1 = 0
    y2 = 0
    y3 = x1

    while True:
        if not invariant_holds(y1, y2, y3, x1, x2):
            break
        y1, y2, y3 = advance_state(y1, y2, y3, x2)

    return None