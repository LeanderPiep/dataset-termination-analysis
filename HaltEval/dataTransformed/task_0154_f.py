# label: f

FEATURE_ENABLED = True

def loop_condition(x, n):
    return x == n * n * n

def update_values(n, x, y, z):
    n = n + 1
    x = x + y
    y = y + z
    z = z + 6
    return n, x, y, z

def main(a):
    if not FEATURE_ENABLED:
        return None

    n = 0
    x = 0
    y = 1
    z = 6

    while loop_condition(x, n):
        n, x, y, z = update_values(n, x, y, z)
    return None