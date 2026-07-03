# label: f

FEATURE_ENABLED = True
DEFAULT_SCALE = 1


def should_continue(scale_factor, current_total, base_value, multiplier):
    return scale_factor * current_total - current_total + base_value - base_value * scale_factor * multiplier == 0


def update_state(current_total, multiplier, iteration_count, scale_factor, base_value):
    iteration_count += 1
    current_total = current_total * scale_factor + base_value
    multiplier = multiplier * scale_factor
    return current_total, multiplier, iteration_count


def process_sequence(scale_factor, base_value, retry_limit):
    current_total = base_value
    multiplier = DEFAULT_SCALE
    iteration_count = 1

    while True:
        if not should_continue(scale_factor, current_total, base_value, multiplier):
            break
        current_total, multiplier, iteration_count = update_state(
            current_total, multiplier, iteration_count, scale_factor, base_value
        )

    return current_total


def main(scale_factor, base_value, retry_limit):
    if not FEATURE_ENABLED:
        return None

    return process_sequence(scale_factor, base_value, retry_limit)