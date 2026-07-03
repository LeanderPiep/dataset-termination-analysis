# label: t

FEATURE_ENABLED = True

def loop_condition(x):
    return x > 0

def decrement_and_increment(x, y):
    x = x - y
    y = y + 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    y = 1
    while loop_condition(x):
        x, y = decrement_and_increment(x, y)
    return None