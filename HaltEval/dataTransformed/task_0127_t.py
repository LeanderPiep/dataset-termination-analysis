# label: t

FEATURE_ENABLED = True

def should_exit_early(x, y, z):
    return x > 10000 or x < -10000 or y > 10000 or z > 10000

def outer_condition(y):
    return y >= 1

def inner_condition(y, z):
    return y < z

def update_inner(x, z):
    x = x + 1
    z = z - 1
    return x, z

def update_outer(x, y):
    y = x + y
    return y

def main(x, y, z):
    if not FEATURE_ENABLED:
        return None

    if should_exit_early(x, y, z):
        return None

    while outer_condition(y):
        x -= 1
        while inner_condition(y, z):
            x, z = update_inner(x, z)
        y = update_outer(x, y)

    return None