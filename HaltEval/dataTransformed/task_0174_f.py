# label: f

FEATURE_ENABLED = True

def loop_condition(i, range_):
    return 0 <= i <= range_

def update_values(i, range_):
    if not (0 == i and i == range_):
        if i == range_:
            i = 0
            range_ = range_ - 1
        else:
            i = i + 1
    return i, range_

def main(i):
    if not FEATURE_ENABLED:
        return None

    range_ = 20
    while loop_condition(i, range_):
        i, range_ = update_values(i, range_)
    return None