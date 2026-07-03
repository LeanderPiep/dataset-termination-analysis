# label: t

FEATURE_ENABLED = True


def update_state(a, b):
    a -= 1
    b = -2 * b
    return a, b


def process_values(a, b):
    while a + b > 0:
        a, b = update_state(a, b)
    return None


def main(value_a, value_b):
    if not FEATURE_ENABLED:
        return None

    return process_values(value_a, value_b)