# label: t

FEATURE_ENABLED = True

def loop_condition(x):
    return x >= 0

def update_values(x, d1, d2):
    x = x - d1
    d1old = d1
    d1 = d2 + 1
    d2 = d1old + 1
    return x, d1, d2

def main(x):
    if not FEATURE_ENABLED:
        return None

    d1 = 73
    d2 = 74

    while loop_condition(x):
        x, d1, d2 = update_values(x, d1, d2)
    return None