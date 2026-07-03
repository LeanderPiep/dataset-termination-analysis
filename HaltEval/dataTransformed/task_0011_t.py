# label: t

FEATURE_ENABLED = True


def update_offsets(left_value, right_value, step_a, step_b):
    left_value = left_value + step_a - step_b - 1
    right_value = right_value + step_b - step_a - 1
    return left_value, right_value


def process_offsets(match_left, match_right, left_value, right_value):
    if match_left != match_right:
        return None

    while left_value >= 0 or right_value >= 0:
        left_value, right_value = update_offsets(left_value, right_value, match_left, match_right)

    return None


def main(match_left, match_right, left_value, right_value):
    if not FEATURE_ENABLED:
        return None

    return process_offsets(match_left, match_right, left_value, right_value)