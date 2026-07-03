# label: f

FEATURE_ENABLED = True


def should_continue(x, y, z):
    return (1 + x * z - x - z * y) == 0


def update_state(x, y, counter, z):
    counter += 1
    x = x * z + 1
    y = y * z
    return x, y, counter


def run_loop(z, limit):
    x = 1
    y = 1
    counter = 1

    while True:
        if not should_continue(x, y, z):
            break
        x, y, counter = update_state(x, y, counter, z)

    return None


def main(z, limit):
    if not FEATURE_ENABLED:
        return None

    return run_loop(z, limit)