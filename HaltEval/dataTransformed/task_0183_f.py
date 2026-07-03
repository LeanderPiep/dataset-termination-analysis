# label: f

FEATURE_ENABLED = True

def loop_condition(a, b):
    return a >= 1 and b >= 1

def update_values(a, b):
    a = 2 * a
    b = 3 * b
    return a, b

def main(a, b):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(a, b):
        a, b = update_values(a, b)
    return None