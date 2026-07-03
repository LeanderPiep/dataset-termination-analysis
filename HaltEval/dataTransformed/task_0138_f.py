# label: f

FEATURE_ENABLED = True

def should_continue(a, b, x, q, y, s):
    return b == x * q + y * s

def update_state(a, b, p, q, r, s):
    if a > b:
        a = a - b
        p = p - q
        r = r - s
    else:
        b = b - a
        q = q - p
        s = s - r
    return a, b, p, q, r, s

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if x >= 1 and y >= 1:
        a = x
        b = y
        p = 1
        q = 0
        r = 0
        s = 1

        while should_continue(a, b, x, q, y, s):
            a, b, p, q, r, s = update_state(a, b, p, q, r, s)

    return None