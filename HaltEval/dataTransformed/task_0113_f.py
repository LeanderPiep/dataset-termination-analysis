# label: f

FEATURE_ENABLED = True

def should_continue(i):
    return i > 0

def update_direction(i, up):
    if i == 1:
        up = 1
    if i == 10:
        up = 0
    return up

def update_value(i, up):
    if up == 1:
        i = i + 1
    else:
        i = i - 1
    return i

def main(i):
    if not FEATURE_ENABLED:
        return None

    up = 0
    while should_continue(i):
        up = update_direction(i, up)
        i = update_value(i, up)
    return None