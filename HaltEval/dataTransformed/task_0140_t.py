# label: t

FEATURE_ENABLED = True

def outer_condition(x):
    return x >= 0

def inner_condition(y, x):
    return y < x

def update_inner(y):
    y = y + 1
    return y

def update_outer(x):
    x = x - 1
    return x

def main(x):
    if not FEATURE_ENABLED:
        return None

    y = 1
    while outer_condition(x):
        while inner_condition(y, x):
            y = update_inner(y)
        x = update_outer(x)
    return None