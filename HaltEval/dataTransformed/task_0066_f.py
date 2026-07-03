# label: f

FEATURE_ENABLED = True


def update_state(x, c):
    x = x - c
    c = c - 1
    return x, c


def main(initial_x, initial_c):
    if not FEATURE_ENABLED:
        return None

    if initial_c < 0:
        x = initial_x
        c = initial_c

        while x + c >= 0:
            x, c = update_state(x, c)

    return None