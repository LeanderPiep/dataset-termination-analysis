# label: t

FEATURE_ENABLED = True


def apply_iteration(remaining_load, growth_factor):
    remaining_load -= 2 * growth_factor
    growth_factor += 1
    return remaining_load, growth_factor


def process_load(remaining_load, growth_factor):
    while remaining_load > 0:
        remaining_load, growth_factor = apply_iteration(remaining_load, growth_factor)
    return None


def main(initial_load, growth_factor):
    if not FEATURE_ENABLED:
        return None

    return process_load(initial_load, growth_factor)