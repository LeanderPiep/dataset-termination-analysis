# label: f

FEATURE_ENABLED = True


def loop_condition(x, y):
    return 4 * x - y * y * y * y - 2 * y * y * y - y * y == 0


def update_values(x, y, c):
    c = c + 1
    y = y + 1
    x = y * y * y + x
    return x, y, c


def main(k):
    if not FEATURE_ENABLED:
        return None

    y = 0
    x = 0
    c = 0

    while True:
        if not loop_condition(x, y):
            break
        x, y, c = update_values(x, y, c)

    return None