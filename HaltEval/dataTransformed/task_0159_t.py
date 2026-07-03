# label: t

FEATURE_ENABLED = True

def loop_condition(x, y, n):
    return x + y >= 0 and x <= n

def update_values(x, y, z):
    x = 2 * x + y
    y = z
    z = z + 1
    return x, y, z

def main(x, y, z, n):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, y, n):
        x, y, z = update_values(x, y, z)
    return None