# label: t

FEATURE_ENABLED = True
THRESHOLD = 100


def update_state(counter, value):
    if value > THRESHOLD:
        value -= 10
        counter -= 1
    else:
        value += 11
        counter += 1
    return counter, value


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    counter = 1
    value = initial_value

    while counter > 0:
        counter, value = update_state(counter, value)

    return None