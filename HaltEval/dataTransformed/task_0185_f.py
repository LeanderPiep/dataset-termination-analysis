# label: f

FEATURE_ENABLED = True

def loop_condition(x, y, z, a, b):
    return z + x * y == a * b

def update_values(x, y, z):
    if y % 2 == 1:
        z = z + x
        y = y - 1
    x = x * 2
    y = y // 2
    return x, y, z

def main(a, b):
    if not FEATURE_ENABLED:
        return None

    if b < 1:
        return None

    x = a
    y = b
    z = 0

    while loop_condition(x, y, z, a, b):
        x, y, z = update_values(x, y, z)
    return None