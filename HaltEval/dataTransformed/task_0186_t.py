# label: t

FEATURE_ENABLED = True

def loop_condition(i):
    return i > 1

def decrement(i):
    i = i - 1
    return i

def main(n):
    if not FEATURE_ENABLED:
        return None

    i = n - 1
    while loop_condition(i):
        i = decrement(i)
    return None