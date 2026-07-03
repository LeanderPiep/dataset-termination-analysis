# label: t

FEATURE_ENABLED = True

def loop_condition(x, y):
    return x >= 0 and x + y >= 0

def update_values(x, y, z):
    x = x + y + z
    y = -z - 1
    return x, y

def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, y):
        x, y = update_values(x, y, z)
    return None