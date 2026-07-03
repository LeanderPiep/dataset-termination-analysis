# label: f

FEATURE_ENABLED = True

def loop_condition():
    return True

def update_value(i):
    if i > 0:
        i = i - 1
    if i < 0:
        i = i + 1
    return i

def main(i):
    if not FEATURE_ENABLED:
        return None

    while loop_condition():
        i = update_value(i)
    return None