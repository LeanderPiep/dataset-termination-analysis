# label: t

FEATURE_ENABLED = True


def update_deltas(delta_primary, delta_secondary):
    previous = delta_primary
    delta_primary = delta_secondary + 1
    delta_secondary = previous + 1
    return delta_primary, delta_secondary


def process_budget(remaining, delta_primary, delta_secondary):
    while remaining >= 0:
        remaining -= delta_primary
        delta_primary, delta_secondary = update_deltas(delta_primary, delta_secondary)
    return None


def main(initial_value, delta_primary, delta_secondary):
    if not FEATURE_ENABLED:
        return None

    return process_budget(initial_value, delta_primary, delta_secondary)