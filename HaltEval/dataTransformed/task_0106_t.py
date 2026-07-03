# label: t

FEATURE_ENABLED = True

def should_continue(x):
    return x < 40

def update_state(x, z):
    if z == 0:
        x = x + 1
    else:
        x = x + 2
    return x

def main(z):
    if not FEATURE_ENABLED:
        return None

    x = 0
    while should_continue(x):
        x = update_state(x, z)
    return None