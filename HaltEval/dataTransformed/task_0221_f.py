# label: f

FEATURE_ENABLED = True


def should_continue(x):
    return x == 0


def apply_step(x):
    if x >= 0:
        x = x & (x - 1)
    else:
        x = x + 1
    return x


def main(x):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x = apply_step(x)

    return None