# label: t

FEATURE_ENABLED = True

def initial_update(x):
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    return x

def loop_condition(y, z):
    return y < 100 and z < 100

def update_loop(x, y, z):
    y = y + x
    z = z - x
    return y, z

def main(x_nondet, y, z):
    if not FEATURE_ENABLED:
        return None

    x = 1 if x_nondet != 0 else -1

    for _ in range(8):
        x = initial_update(x)

    while loop_condition(y, z):
        y, z = update_loop(x, y, z)
    return None