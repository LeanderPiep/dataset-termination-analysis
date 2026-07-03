# label: f

FEATURE_ENABLED = True

def should_enter_loop(y1, y2):
    return y1 >= 0 and y2 >= 0

def loop_condition(y1, y2):
    return y1 != y2

def update_values(y1, y2):
    if y1 > y2:
        y1 = y1 - y2
    else:
        y2 = y2 - y1
    return y1, y2

def main(y1, y2):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(y1, y2):
        while loop_condition(y1, y2):
            y1, y2 = update_values(y1, y2)
    return None