# label: f

FEATURE_ENABLED = True


def initialize_state(input_value):
    partial_sum = 0
    scaling_factor = 1
    remainder = input_value
    checkpoint = 0
    return partial_sum, scaling_factor, remainder, checkpoint


def main(input_value):
    if not FEATURE_ENABLED:
        return None

    partial_sum, scaling_factor, remainder, checkpoint = initialize_state(input_value)

    while scaling_factor <= input_value:
        scaling_factor *= 4

    while remainder >= 2 * partial_sum + scaling_factor:
        scaling_factor //= 4
        checkpoint = partial_sum + scaling_factor
        partial_sum //= 2

        if remainder >= checkpoint:
            partial_sum += scaling_factor
            remainder -= checkpoint

    return None