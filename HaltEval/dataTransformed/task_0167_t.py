# label: t

FEATURE_ENABLED = True

def outer_condition(x1):
    return x1 <= 10

def inner_condition(x2):
    return x2 > 1

def decrement_x2(x2):
    x2 = x2 - 1
    return x2

def increment_x1(x1):
    x1 = x1 + 1
    return x1

def main(x1, x2):
    if not FEATURE_ENABLED:
        return None

    while outer_condition(x1):
        x2 = 10
        while inner_condition(x2):
            x2 = decrement_x2(x2)
        x1 = increment_x1(x1)
    return None