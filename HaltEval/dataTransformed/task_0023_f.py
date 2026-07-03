# label: f

FEATURE_ENABLED = True


def update_state(value, delta, growth):
    value = value + delta
    delta = delta + growth
    growth = growth + value
    return value, delta, growth


def main(initial_value, delta, growth):
    if not FEATURE_ENABLED:
        return None

    value = initial_value

    while value > 0:
        value, delta, growth = update_state(value, delta, growth)

    return None