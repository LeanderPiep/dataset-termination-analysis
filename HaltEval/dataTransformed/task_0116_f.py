# label: f

FEATURE_ENABLED = True

def invariant_holds(x, y):
    return 6 * y**5 + 15 * y**4 + 10 * y**3 - 30 * x - y == 0

def update_state(c, x, y):
    c = c + 1
    y = y + 1
    x = y**4 + x
    return c, x, y

def main(k):
    if not FEATURE_ENABLED:
        return None

    y = 0
    x = 0
    c = 0

    while True:
        if not invariant_holds(x, y):
            break
        c, x, y = update_state(c, x, y)

    return None