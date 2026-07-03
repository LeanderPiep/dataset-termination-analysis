# label: f

FEATURE_ENABLED = True


def update_state(counter, acc_x, acc_y, step):
    counter += 1
    acc_x += acc_y
    acc_y += step
    step += 6
    return counter, acc_x, acc_y, step


def main(input_value):
    if not FEATURE_ENABLED:
        return None

    counter = 0
    acc_x = 0
    acc_y = 1
    step = 6

    while step <= 6 * counter + 6:
        counter, acc_x, acc_y, step = update_state(counter, acc_x, acc_y, step)

    return None