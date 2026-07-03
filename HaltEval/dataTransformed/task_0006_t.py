# label: t

FEATURE_ENABLED = True


def normalize_step(step):
    if step < 1:
        return None
    return step


def decrement_until_negative(value, step):
    while value >= 0:
        value -= step
    return None


def main(initial_value, step):
    if not FEATURE_ENABLED:
        return None

    step = normalize_step(step)
    if step is None:
        return None

    return decrement_until_negative(initial_value, step)