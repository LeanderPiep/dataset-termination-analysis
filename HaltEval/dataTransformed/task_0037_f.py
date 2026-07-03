# label: f

FEATURE_ENABLED = True


def update_state(i, direction_flag):
    if i == 10:
        direction_flag = 0
    if i == 0:
        direction_flag = 1

    if direction_flag == 1:
        i += 1
    else:
        i -= 1

    return i, direction_flag


def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    i = initial_value
    direction_flag = 0

    while 0 <= i <= 10:
        i, direction_flag = update_state(i, direction_flag)

    return None