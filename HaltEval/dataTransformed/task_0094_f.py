# label: f

FEATURE_ENABLED = True

def is_in_range(x):
    return x <= 23 and x >= -42

def recursive_step(x, y):
    return 2 * y - 2, x + 1

def process_recursive(x, y):
    if is_in_range(x):
        new_x, new_y = recursive_step(x, y)
        process_recursive(new_x, new_y)

def main(n):
    if not FEATURE_ENABLED:
        return None

    if n <= 2147483646:
        process_recursive(n, n + 1)
    return None