# label: f

FEATURE_ENABLED = True

def should_continue(x):
    return x != 0

def update_state(x):
    if -5 <= x <= 35:
        if x < 0:
            x = -5
        else:
            if x > 30:
                x = 35
            else:
                x = x - 1
    else:
        x = 0
    return x

def main(x):
    if not FEATURE_ENABLED:
        return None

    while should_continue(x):
        x = update_state(x)
    return None