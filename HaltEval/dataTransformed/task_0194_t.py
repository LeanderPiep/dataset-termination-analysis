# label: t

FEATURE_ENABLED = True

def precheck(m, n, r):
    return m >= 0 and n >= 0 and r >= 0

def recursive_case(m, n, r):
    if r > 0:
        return recursive_case(m, r-1, n)
    elif n > 0:
        return recursive_case(r, n-1, m)
    else:
        return m

def main(m, n, r):
    if not FEATURE_ENABLED:
        return None

    if not precheck(m, n, r):
        return None

    return recursive_case(m, n, r)