# label: f

FEATURE_ENABLED = True


def is_valid_input(a, b):
    return 1 <= a <= 65535 and 1 <= b <= 65535


def loop_condition(x, y, u, v, a, b):
    return x * u + y * v == 2 * a * b


def update_values(x, y, u, v):
    if x > y:
        x = x - y
        v = v + u
    else:
        y = y - x
        u = u + v
    return x, y, u, v


def main(a, b):
    if not FEATURE_ENABLED:
        return None

    if not is_valid_input(a, b):
        return None

    x = a
    y = b
    u = b
    v = a

    while True:
        if not loop_condition(x, y, u, v, a, b):
            break
        x, y, u, v = update_values(x, y, u, v)

    return None