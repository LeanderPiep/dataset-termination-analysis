# label: f

FEATURE_ENABLED = True

def loop_condition(y):
    return y != 0

def update_values(x, y):
    tmp = y
    xtmp = x

    if x <= 0 or y <= 0:
        y = 0
    elif x == y:
        y = 0
    else:
        while xtmp > y:
            xtmp = xtmp - y

    y = xtmp
    x = tmp
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    while loop_condition(y):
        x, y = update_values(x, y)
    return None