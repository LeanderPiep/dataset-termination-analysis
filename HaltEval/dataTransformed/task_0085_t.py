# label: t

FEATURE_ENABLED = True


def grow_to_limit(current_value, limit_value):
    while current_value < limit_value:
        current_value = 2 * current_value
    return current_value


def main(n, y):
    if not FEATURE_ENABLED:
        return None

    x = n

    if x >= 0:
        while x >= 0:
            y = 1
            if y < x:
                y = grow_to_limit(y, x)
            x = x - 1

    return None