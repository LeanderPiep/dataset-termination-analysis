# label: f

FEATURE_ENABLED = True

def outer_condition(b):
    return b != 0

def inner_condition_c(c, b):
    return c >= b

def innermost_condition(b, x, q, y, s):
    return b == x * q + y * s

def update_innermost(d, v, b):
    d = 2 * d
    v = 2 * v
    return d, v

def update_inner(c, k, v, d):
    c = c - v
    k = k + d
    return c, k

def update_outer(a, b, p, q, r, s, k):
    a, b = b, a
    temp = p
    p = q
    q = temp - q * k
    temp = r
    r = s
    s = temp - s * k
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

    while outer_condition(b):
        c = a
        k = 0

        while inner_condition_c(c, b):
            d = 1
            v = b
            while innermost_condition(b, x, q, y, s):
                d, v = update_innermost(d, v, b)
            c, k = update_inner(c, k, v, d)

        a, b, p, q, r, s = update_outer(a, b, p, q, r, s, k)

    return None