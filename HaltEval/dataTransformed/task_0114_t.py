# label: t

FEATURE_ENABLED = True

def initialize_step(b):
    if b >= 1:
        return 1
    return -1

def should_continue(x, n):
    return x <= n

def update_position(x, t, b):
    if b >= 1:
        x = x + t
    else:
        x = x - t
    return x

def main(i, x, n, b):
    if not FEATURE_ENABLED:
        return None

    t = initialize_step(b)
    while should_continue(x, n):
        x = update_position(x, t, b)
    return None