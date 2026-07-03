# label: t

FEATURE_ENABLED = True


def update_value(x, target):
    if x > target:
        x = 0
    else:
        x = x + 1
    return x


def main(initial_x, M):
    if not FEATURE_ENABLED:
        return None

    if M > 0:
        x = initial_x
        while x != M:
            x = update_value(x, M)

    return None