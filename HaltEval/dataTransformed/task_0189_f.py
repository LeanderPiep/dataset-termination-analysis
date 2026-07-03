# label: f

FEATURE_ENABLED = True

def loop_condition(d, k, t, a):
    return d * k - d * t - a * k + a * t == 0

def update_values_case1(r, q, k, t, d):
    t = r
    r = 2 * r - k + q + d + 2
    k = t
    q = q + 4
    d = d + 2
    return r, q, k, t, d

def update_values_case2(r, q, k, t, d):
    t = r
    r = 2 * r - k + q
    k = t
    d = d + 2
    return r, q, k, t, d

def update_values_case3(r, q, k, t, d):
    t = r
    r = 2 * r - k + q - d - 2
    k = t
    q = q - 4
    d = d + 2
    return r, q, k, t, d

def update_values_case4(r, q, k, t, d):
    t = r
    r = 2 * r - k + q - 2 * d - 4
    k = t
    q = q - 8
    d = d + 2
    return r, q, k, t, d

def main(s, a):
    if not FEATURE_ENABLED:
        return None

    if s >= 8192:
        return None
    if a <= 2:
        return None

    n = s * s
    d = a
    r = n % d
    t = 0
    k = n % (d - 2)
    q = 4 * (n / (d - 2) - n / d)

    while loop_condition(d, k, t, a):
        expr = 2 * r + q
        if expr < k:
            r, q, k, t, d = update_values_case1(r, q, k, t, d)
        elif expr >= k and expr < d + k + 2:
            r, q, k, t, d = update_values_case2(r, q, k, t, d)
        elif expr >= k and expr >= d + k + 2 and expr < 2 * d + k + 4:
            r, q, k, t, d = update_values_case3(r, q, k, t, d)
        else:
            r, q, k, t, d = update_values_case4(r, q, k, t, d)

    return None