# label: f

FEATURE_ENABLED = True


def update_state(sum_value, counter):
    sum_value += 2
    counter += 1
    return sum_value, counter


def invariant_holds(sum_value, counter):
    return sum_value == counter * 2 or sum_value == 0


def main(loop_flag, n):
    if not FEATURE_ENABLED:
        return None

    sum_value = 0
    counter = 0

    while True:
        sum_value, counter = update_state(sum_value, counter)

        if not invariant_holds(sum_value, counter):
            return "error"

    return None