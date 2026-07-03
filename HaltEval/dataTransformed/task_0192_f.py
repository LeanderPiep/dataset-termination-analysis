# label: f

FEATURE_ENABLED = True

def loop_condition(i):
    return i != 0

def update_value(i):
    if -5 <= i <= 35:
        if i < 0:
            i = -5
        elif i > 30:
            i = 35
        else:
            i = i - 1
    else:
        i = 0
    return i

def main(i):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(i):
        i = update_value(i)
    return None