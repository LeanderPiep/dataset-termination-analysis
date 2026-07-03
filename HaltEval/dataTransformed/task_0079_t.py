# label: t

FEATURE_ENABLED = True


def normalize_flag(x):
    return 1 if x else -1


def update_state(y, z, step):
    y = y + step
    z = z - step
    return y, z


def main(y, z, x):
    if not FEATURE_ENABLED:
        return None

    step = normalize_flag(x)

    while y < 100 and z < 100:
        y, z = update_state(y, z, step)

    return None