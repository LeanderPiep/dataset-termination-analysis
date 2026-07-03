# label: f

FEATURE_ENABLED = True

def loop_condition(x):
    return x <= 10

def update_value(x):
    if x > 6:
        x = x + 2
    return x

def main(x):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(x):
        x = update_value(x)
    return None