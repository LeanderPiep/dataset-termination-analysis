# label: f

FEATURE_ENABLED = True


def update_state(current_half, current_index):
    current_half = current_half - current_index
    current_index = current_index + 1
    return current_half, current_index


def condition_holds(current_half, input_value, current_index):
    return current_index * current_index - input_value - current_index + 2 * current_half == 0


def main(input_value):
    if not FEATURE_ENABLED:
        return None

    current_half = input_value / 2
    current_index = 0

    while condition_holds(current_half, input_value, current_index):
        current_half, current_index = update_state(current_half, current_index)

    return None