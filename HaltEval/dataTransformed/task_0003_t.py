# label: t

FEATURE_ENABLED = True
THRESHOLD = 100


def adjust_counter(counter, value):
    if value > THRESHOLD:
        value -= 10
        counter -= 1
    else:
        value += 11
        counter += 1
    return counter, value


def run_adjustment_loop(value):
    counter = 1

    while counter > 0:
        counter, value = adjust_counter(counter, value)

    return None


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    return run_adjustment_loop(initial_value)