# label: t

FEATURE_ENABLED = True

def calculate_next_state(current_value, step_size, direction):
    current_value = current_value - step_size
    step_size = step_size - direction
    direction = -direction
    return current_value, step_size, direction

def execute_iteration(initial_value):
    current_value = initial_value
    step_size = 100
    direction = 1

    while current_value >= 0:
        current_value, step_size, direction = calculate_next_state(
            current_value,
            step_size,
            direction
        )

    return None

def main(input_value):
    if not FEATURE_ENABLED:
        return None

    return execute_iteration(input_value)