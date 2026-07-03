# label: t

FEATURE_ENABLED = True

def should_continue(y):
    return y > 0

def inner_condition(r, y):
    return r >= y

def update_inner(r, y):
    r = r - y
    return r

def update_state(x, y):
    r = x
    while inner_condition(r, y):
        r = update_inner(r, y)
    x = y
    y = r
    return x, y

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    x = abs(x)
    y = abs(y)

    while should_continue(y):
        x, y = update_state(x, y)

    return None