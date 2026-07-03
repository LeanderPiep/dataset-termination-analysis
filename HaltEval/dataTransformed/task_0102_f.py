# label: f

FEATURE_ENABLED = True

def should_continue(a):
    return a >= 7

def rotate_values(a, b):
    previous_a = a
    a = b
    b = previous_a + 1
    return a, b, previous_a

def main(a, b):
    if not FEATURE_ENABLED:
        return None

    olda = a
    while should_continue(a):
        a, b, olda = rotate_values(a, b)
    return None