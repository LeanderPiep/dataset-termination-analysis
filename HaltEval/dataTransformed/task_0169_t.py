# label: t

FEATURE_ENABLED = True

def initialize_step(b):
    return 1 if b >= 1 else -1

def loop_condition(x, n):
    return x <= n

def update_value(x, t, b):
    if b >= 1:
        x = x + t
    else:
        x = x - t
    return x

def main(x, n, b):
    if not FEATURE_ENABLED:
        return None

    t = initialize_step(b)

    while loop_condition(x, n):
        x = update_value(x, t, b)
    return None