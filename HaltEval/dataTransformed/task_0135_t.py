# label: t

FEATURE_ENABLED = True

def precheck(x, y):
    return x >= 0 and y >= 0

def recursive_f(x, y):
    if y == 0:
        return x
    if x == 0:
        return recursive_f(y, y-1)
    return recursive_f(y, x-1)

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if not precheck(x, y):
        return None

    return recursive_f(x, y)