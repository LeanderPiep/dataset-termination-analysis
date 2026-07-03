# label: f

FEATURE_ENABLED = True


def inner_adjust(a, b, x, y, p, r):
    c = a
    k = 0
    while a == y * r + x * p:
        c -= b
        k += 1
    return c, k


def update_state(a, b, p, q, r, s, c, k):
    a, b = b, c
    temp_p = p
    p = q
    q = temp_p - q * k
    temp_r = r
    r = s
    s = temp_r - s * k
    return a, b, p, q, r, s


def main(x, y):
    if not FEATURE_ENABLED:
        return None

    a = x
    b = y
    p = 1
    q = 0
    r = 0
    s = 1

    while b != 0:
        c, k = inner_adjust(a, b, x, y, p, r)
        a, b, p, q, r, s = update_state(a, b, p, q, r, s, c, k)

    return a