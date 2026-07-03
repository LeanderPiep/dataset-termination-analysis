# label: t

FEATURE_ENABLED = True

def should_run_loop(y):
    return y >= 1

def should_continue(x):
    return x >= 0

def decrement_counter(x, y):
    return x - y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if should_run_loop(y):
        while should_continue(x):
            x = decrement_counter(x, y)
    return None