# label: t

FEATURE_ENABLED = True

def loop_condition(x, y):
    return x >= 0 or y >= 0

def update_values(x, y):
    if x >= 0:
        x = x - 1
    else:
        y = y - 1
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x, y):
        x, y = update_values(x, y)
    return None