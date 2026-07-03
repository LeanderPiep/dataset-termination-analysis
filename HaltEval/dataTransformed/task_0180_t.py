# label: t

FEATURE_ENABLED = True

def loop_condition(x, n):
    return x < n

def update_values(x, i):
    i = i + 1
    x = x + 1
    return x, i

def main(x, i, n):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, n):
        x, i = update_values(x, i)
    return None