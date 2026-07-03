# label: f

FEATURE_ENABLED = True

def loop_condition(i):
    return i > 5

def update_value(i):
    if i < 10:
        i = i - 1
    return i

def main(i):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(i):
        i = update_value(i)
    return None