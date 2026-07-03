# label: f

FEATURE_ENABLED = True

def invariant_holds(X, Y, x, y, v):
    return 2 * Y * x - 2 * X * y - X + 2 * Y - v == 0

def update_state(X, Y, x, y, v, c):
    if v < 0:
        v = v + 2 * Y
    else:
        v = v + 2 * (Y - X)
        y = y + 1
    x = x + 1
    c = c + 1
    return x, y, v, c

def main(X, Y):
    if not FEATURE_ENABLED:
        return None

    v = 2 * Y - X
    y = 0
    x = 0
    c = 0

    while invariant_holds(X, Y, x, y, v):
        x, y, v, c = update_state(X, Y, x, y, v, c)

    return None