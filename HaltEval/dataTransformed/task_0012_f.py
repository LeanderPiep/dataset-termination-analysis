# label: f

FEATURE_ENABLED = True


def update_state(value, delta, increment):
    value = value + delta
    delta = delta + increment
    return value, delta


def process_loop(value, delta, increment):
    while value > 0:
        value, delta = update_state(value, delta, increment)
    return None


def main(initial_value, delta, increment):
    if not FEATURE_ENABLED:
        return None

    return process_loop(initial_value, delta, increment)