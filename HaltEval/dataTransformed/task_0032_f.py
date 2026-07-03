# label: f

FEATURE_ENABLED = True


def should_continue(x, y, scale_factor):
    return x * scale_factor - x - y + 1 == 0


def update_state(x, y, iteration_count, scale_factor):
    iteration_count += 1
    x = x * scale_factor + 1
    y = y * scale_factor
    return x, y, iteration_count


def main(scale_factor, retry_limit):
    if not FEATURE_ENABLED:
        return None

    x = 1
    y = scale_factor
    iteration_count = 1

    while True:
        if not should_continue(x, y, scale_factor):
            break
        x, y, iteration_count = update_state(x, y, iteration_count, scale_factor)

    x = x * (scale_factor - 1)
    return None