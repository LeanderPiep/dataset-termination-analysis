# label: t

FEATURE_ENABLED = True

def should_continue(a):
    return a >= 0

def update_state(a, b):
    a = a + b
    if b >= 0:
        b = -b - 1
    else:
        b = -b
    return a, b

def main(a, b):
    if not FEATURE_ENABLED:
        return None

    while should_continue(a):
        a, b = update_state(a, b)
    return None